"""
Projeto ISA
"""
import datetime
import json
import re
import os
from time import sleep 
import hashlib
import pymysql
import sqlparse 
import boto3 
from IPython.core import magic_arguments 
from IPython.core.magic import Magics 
from delta.tables import DeltaTable 
 
AWS_REGION    = os.environ.get('AWS_REGION','us-east-1') 
STATE_MACHINE = os.environ.get('AWS_STATE_MACHINE','arn:aws:states:us-east-1:229343956935:stateMachine:benny-import-data') 
BENNY_ARN     = os.environ.get('BENNY_ARN','arn:aws:lambda:us-east-1:229343956935:function:benny') 
CACHE_DB      = os.environ.get('CACHE_DB','cache') 
DELTA_DB      = os.environ.get('DELTA_DB','delta') 
DORA_BUCKET   = os.environ.get('S3_BUCKET','autonomous-sandbox') 
ADHOC_DB      = os.environ.get('ADHOC_DB','adhoc') 
DORA_USER     = os.environ.get('DORA_USER') 
INSTANCE_TYPE = os.environ.get('INSTANCE_TYPE','P') 
DORA_STORAGE  = os.environ.get('DORA_STORAGE','s3a')
 
class ISAContext: 
    """ 
    Contextualiza as consultas a serem executadas 
    """ 
    r_date=r"""'([0-9]{4}-[0-9]{2}-[0-9]{2})'""" 
    r_user_connections = r"""^show[\s]*connections$"""
    r_cache_tables = r"""^show[\s]*cache$"""
    r_version=r"""'[0-9]{1,}'""" 
    r_table = r"""(?:[\s]+)([\d\w\$_]+\.[\d\w\$_]+\.[\d\w\$_]+)(?:(?:[\s])+|\Z|;|\))""" 
    r_create = r"""CREATE\s+?TABLE\s+?(?:(?:IF NOT EXISTS)(.+?)|(.+?))\s+?AS\s+SELECT(.)+;?"""
    r_select = f"""[\s]?(FROM|JOIN)[\s]?{r_table}""" 
    r_d_table = r"""DROP[\s]+TABLE(?:[\s]+IF[\s]+EXISTS)?[\s]+(([\d\w\$_]+)|([\d\w\$_]+\.[\d\w\$_]+))(?:(?:[\s])+|\Z|;|\))"""
    r_drop = f"""DROP[\s]?TABLE[\s]?{r_table}""" 
    r_delta = f"""{r_table}(asof+)(?:(?:[\s])+|\Z|\))({r_date}|{r_version})""" 

    table_status ="""SELECT * FROM isa.table_status WHERE full_name_table = %s """ 
    log_dora = """INSERT INTO `isa`.`log_dora` (`timestamp`, `instance`, `query`, `query_raw`, `total_time_execution`, `total_time_query`,`user`, `type_instance_dora`, 
            `type_instance_aws`, `table_list`, `table_log`, `exist_error`, `code_error`, `execution`, `parameters_args`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" 
     
    def __init__(self,spark,debug=False): 
        """ 
        Parameters 
        ---------- 
        spark : object 
            recebe o contexto spark 
        schema : str 
            default: 'cache' 
            Identificador do schema de chache no metastore do dora 
        debug : boolean 
            quando true ativa o modo debug 
        """ 
        
        self.spark = spark 
        self.sc = spark.sparkContext 
        self.debug = debug 
        self.steps = boto3.client('stepfunctions',AWS_REGION)
         
    def printd(self,*messages): 
        """ 
        Utilitário usado para exibir as mensagem quando o modo debug está ativado 
        ---------- 
        messages : list 
            Lista de todas as mensagems a serem printadas  
        """ 
        if self.debug: 
            for message in messages: 
                print(message) 
     
    def get_table_status(self,table_list): 
        """ 
        Consulta os metadados das tabelas solicitadas no Dora Metastore 
        ---------- 
        table_list : list 
            Lista de todas as tabelas solicitadas na query  
        Returns 
        ------- 
        Dict 
            Retorna um dicionário com os metadados de todas as tabelas solicitadas 
        """ 
        connection = pymysql.connect( host=os.environ['HIVE_BASE'] 
                                    , user=os.environ['HIVE_USER'] 
                                    , password=os.environ['HIVE_PASS'] 
                                    , db='isa',cursorclass=pymysql.cursors.DictCursor) 
        tables_log_meta = [] 
        table_log = dict() 
        table_meta = dict() 
        try: 
            with connection.cursor() as cursor: 
                for table_id in table_list: 
                    cursor.execute(self.table_status, (table_id.upper().replace('.','_'),)) 
                    table_meta[table_id] = cursor.fetchone() 
                    if table_meta[table_id] is not None: 
                        cond = 'full load'
                        if table_meta[table_id].get('condition') is not None:
                            cond = f"""load condition \"{table_meta[table_id].get('condition')}\""""
                        if table_meta[table_id].get('nextUpdate') <= datetime.datetime.now(): 
                            print(f"{table_id} is outdated: {table_meta[table_id].get('lastUpdate')} ({table_meta[table_id].get('cacheDays')} days)") 
                            table_log[table_id] = f"{table_id} is outdated: {table_meta[table_id].get('lastUpdate')} ({table_meta[table_id].get('cacheDays')} days)" 
                            table_meta[table_id] = None 
                        else: 
                            print(f"{table_id} is updated: {table_meta[table_id].get('lastUpdate')} ({table_meta[table_id].get('cacheDays')} days)") 
                            table_log[table_id] = f"{table_id} is updated: {table_meta[table_id].get('lastUpdate')} ({table_meta[table_id].get('cacheDays')} days)" 
                            table_meta[table_id]['outdated'] = False 
                    else: 
                        print(f"{table_id} is now loading") 
                        table_log[table_id] = f"{table_id} is now loading" 
                        table_meta[table_id] = {'outdated':True}
            tables_log_meta.append(table_meta) 
            tables_log_meta.append(table_log) 
            return tables_log_meta 
        finally: 
            connection.close() 
     
    def load_tables(self, table_list, table_meta): 
        """ 
        Agenda a execução de todas as tableas que precisam ser atualizadas 
        ---------- 
        table_list : list 
            Lista de todas as tabelas desatualizadas  
        Returns 
        ------- 
        List 
            Retorna a lista das execuções agendadas via Step-Function 
        """ 
        responses=list() 
        for table_id in table_list: 
            conn,schema,table=table_id.split('.') 
            input_data={"username": os.environ['DORA_USER'],"connection_name": conn,"schema": schema,"table": table}
            meta = table_meta.get(table_id)
            if meta is not None:
                input_data["condition"] = meta.get("condition")
                input_data["partition"] = meta.get("partition")
            self.printd('load_tables:input_data:',input_data)
            response=self.steps.start_execution(stateMachineArn=STATE_MACHINE,input=json.dumps(input_data)) 
            responses.append(response) 
        return responses      
    def wait_execution(self, executions): 
        """ 
        Verifica o andamento das Step-Functions em execução 
        ---------- 
        executions : list 
            Lista de todas as execuções em andamento  
        Returns 
        ------- 
        List 
            Retorna a lista das execuções concluídas 
        """ 
        responses=list() 
        while len(executions) > 0: 
            sleep(2) 
            for execution in executions: 
                execution_status=self.steps.describe_execution(executionArn=execution['executionArn']) 
                if execution_status.get('status') != 'RUNNING': 
                    responses.append(execution_status) 
                    input_data = json.loads(execution_status['input']) 
                    self.printd('execution_status',execution_status) 
                    cache_table = f"{CACHE_DB}.{input_data['connection_name']}_{input_data['schema']}_{input_data['table']}" 
                    self.spark.sql(f"REFRESH TABLE {cache_table}") 
                    executions.remove(execution) 
        return responses 
     
    def creat_version_of(self, table, version, alias): 
        """ 
        Consulta as versões de uma determinada tabela 
        ---------- 
        table : string 
            Nome interno da tabela no databse cache 
        version : string 
            Numero da versão ou data que se deseja consultar 
        alias : string 
            Nome funcional da tabela, para apresentação 
        Returns 
        ------- 
        string 
            Nome da tabela temporária contendo os dados da versão solicitada 
        """ 
        c,s,t = table.split('.') 
        delta_path = f"s3a://{DORA_BUCKET}/{DELTA_DB}/{c}_{s}_{t}" 
        table_history = f"h_{c}_{s}_{t}" 
        try: 
            self.spark.catalog.isCached(table_history) 
        except: 
            DeltaTable.forPath(self.spark, delta_path).history().createOrReplaceTempView(table_history) 
        try: 
            v = re.findall(self.r_version,version,re.IGNORECASE)[0].replace("'","") 
            r = self.spark.sql(f"""SELECT * FROM ( 
                              SELECT timestamp `dt`,version `v` FROM {table_history} WHERE version = {v} UNION ALL 
                              SELECT timestamp `dt`,version `v` FROM {table_history} WHERE version = 0) ORDER BY 2 DESC""").take(1) 
        except: 
            dt = re.findall(self.r_date,version,re.IGNORECASE)[0] 
            r = self.spark.sql(f"""SELECT * FROM(SELECT * FROM (SELECT max(timestamp)`dt`,max(version)`v` FROM {table_history} WHERE date_trunc('DD',timestamp)<='{dt}'  
                              GROUP BY date_trunc('DD',timestamp) ORDER BY 1 DESC LIMIT 1) UNION ALL SELECT timestamp `dt`,version `v` FROM {table_history} WHERE version = 0) ORDER BY 2 DESC""").take(1) 
        v = r[0].v 
        table_name = f"v{v}_{c}_{s}_{t}" 
        print(f"{alias} -> {r[0].dt.strftime('%Y-%m-%d %H:%M:%S')}") 
        try: 
            self.spark.catalog.isCached(table_name) 
        except: 
            self.spark.read.format("delta").option("versionAsOf", v).load(delta_path).createOrReplaceTempView(table_name) 
        return table_name 
     
    def sql_parser(self, sql): 
        """ 
        Realiza o parser do SQL utilizado para geração do HASH 
        ---------- 
        sql : string 
            Recebe a query bruta. 
        Returns 
        ------- 
        list 
            Retorna a lista de todos os itens da query formatados 
        """ 
        p = sqlparse.parse(sql) 
        for s in sqlparse.parse(sql): 
            if s.get_type() != 'SELECT': 
                raise ValueError(f"Only 'SELECT' statements are allowed") 
            q = list() 
            for k,v in enumerate(s.tokens): 
                if v.is_whitespace: 
                    continue 
                if v.is_keyword: 
                    q.append(v.normalized.upper()) 
                else: 
                    q.append(v.normalized) 
            return q 
 
    def __save_table_query(self, query):
        connection = pymysql.connect( host=os.environ['HIVE_BASE'] 
                                    , user=os.environ['HIVE_USER'] 
                                    , password=os.environ['HIVE_PASS'] 
                                    , db='isa', cursorclass=pymysql.cursors.DictCursor) 
        try: 
            table_name = re.search(self.r_create, query, re.MULTILINE | re.IGNORECASE)
            tables_list = [x for _, x in re.findall(self.r_select, query, re.MULTILINE | re.IGNORECASE)]
            tables_affected = dict(tables=tables_list) if tables_list else {}
            table_active = 1
            table_name = table_name.group(1).strip() if re.search(r"IF NOT EXISTS", query, re.MULTILINE | re.IGNORECASE) else table_name.group(2).strip()
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM isa.user_tables WHERE table_name='{table_name}' AND active=0")
                data = cursor.fetchone()
                if data: 
                    cursor.execute(f"""UPDATE isa.user_tables SET query='{query}', active={table_active}, timestamp=now() where table_name='{table_name}'""")
                    connection.commit()
                    return None
                
                cursor.execute(f"SELECT * FROM isa.user_tables WHERE table_name='{table_name}'")
                data = cursor.fetchone()
                if data:
                    return None
                
                insert = "INSERT INTO isa.user_tables (table_name, query, affected_tables, active) VALUES (%s,%s,%s,%s)"
                cursor.execute(insert, (table_name, query, json.dumps(tables_affected), table_active))
                connection.commit()          
        finally:
            connection.close() 
        
 
    def __sql_log(self, attributes): 
        """ 
            Performs the insert of Dora logs in the database, schema isa: Private function 
            ---------- 
            attributes : dict 
                Are all attributes required to insert from logs 
            Returns 
            ------- 
            Not have return 
        """ 
 
        timestamp = attributes["timestamp"] 
        query = attributes["query"] if "query" in attributes else None 
        table_list = str(attributes["table_list"]) if "table_list" in attributes else None 
        table_log = json.dumps(attributes["table_log"]) if "table_log" in attributes else None 
        exist_error = str(attributes["exist_error"]) if "exist_error" in attributes else None 
        code_error = str(attributes["code_error"]) if "code_error" in attributes else None 
        execution = str(attributes["execution"]) if "execution" in attributes else None 
 
        connection = pymysql.connect(host=os.environ['HIVE_BASE'] 
                                     , user=os.environ['HIVE_USER'] 
                                     , password=os.environ['HIVE_PASS'] 
                                     , db='isa', cursorclass=pymysql.cursors.DictCursor) 
        try: 
            with connection.cursor() as cursor: 
                cursor.execute(self.log_dora, (timestamp, attributes["instance"], query, attributes["query_raw"], 
                                               attributes["total_time_execution"], attributes["total_time_query"], 
                                               attributes["user"],attributes["type_instance_dora"], 
                                               attributes["type_instance_aws"], table_list, table_log, 
                                               exist_error, code_error, execution, str(attributes["parameters_args"]))) 
                connection.commit() 
        finally: 
            connection.close() 
 
 
    def sql(self, query, **kwargs): 
        """ 
        Executa query usando SparkSQL 
        ---------- 
        query : string 
            Recebe a query bruta. 
        kwargs : dict 
            Argumentos enviados pelo usuário pelo Magic Comand 
        Returns 
        ------- 
        Dataframe 
            retorna o dataframe da query. 
        """ 
 
        attributes_log = dict() 
        timestamp = datetime.datetime.now() 
        instance = os.popen('curl -sL "http://169.254.169.254/latest/meta-data/instance-id"').read() 
        type_instance_aws = os.popen('curl -sL "http://169.254.169.254/latest/meta-data/instance-type"').read() 
 
        attributes_log["timestamp"] = timestamp 
        attributes_log["parameters_args"] = kwargs 
        attributes_log["query_raw"] = query 
        attributes_log["instance"] = instance 
        attributes_log["type_instance_dora"] = INSTANCE_TYPE 
        attributes_log["type_instance_aws"] = type_instance_aws 
        attributes_log["user"] = DORA_USER 
 
        query = query.replace("workspace://", f"{DORA_STORAGE}://{DORA_BUCKET}/workspaces/{DORA_USER}/")
        query = query.replace("cloud://", f"{DORA_STORAGE}://{DORA_BUCKET}/workspaces/{DORA_USER}/")
 
        self.debug = kwargs.get("verbose")
        self.printd(kwargs)
        
        if kwargs.get("connection") is not None: 
            parser = self.sql_parser(query) 
            table_name = hashlib.sha1(''.join(parser).encode('utf8')).hexdigest() 
            try: 
                if kwargs.get("refresh"):
                    self.spark.sql(f"DROP TABLE IF EXISTS {ADHOC_DB}.{table_name}")
                    self.spark.sql(f"REFRESH TABLE {ADHOC_DB}.{table_name}")
                time_before_spark = datetime.datetime.now() 
                data_frame_spark = self.spark.table(f"{ADHOC_DB}.{table_name}") 
                time_after_spark = datetime.datetime.now() 
 
                attributes_log["total_time_execution"] = (time_after_spark - timestamp).total_seconds() 
                attributes_log["total_time_query"] = (time_after_spark - time_before_spark).total_seconds() 
                self.printd(attributes_log) 
                self.__sql_log(attributes_log) 
 
                return data_frame_spark
            except:
                client = boto3.client('lambda',AWS_REGION) 
                payload = {"adhoc": True,"username": DORA_USER,"connection_name": kwargs.get("connection"),"schema": ADHOC_DB,"table": table_name,"query": query.replace("\n"," ")} 
                self.printd(json.dumps(payload)) 
                response = client.invoke( 
                    FunctionName=BENNY_ARN, 
                    InvocationType='RequestResponse', 
                    Payload=bytes(json.dumps(payload).encode('utf8'))) 
                self.printd(response) 
                self.printd(response.get('Payload').read().decode('utf8')) 
                
                time_before_spark = datetime.datetime.now() 
                data_frame_spark = self.spark.table(f"{ADHOC_DB}.{table_name}") 
                time_after_spark = datetime.datetime.now() 

                attributes_log["total_time_execution"] = (time_after_spark - timestamp).total_seconds() 
                attributes_log["total_time_query"] = (time_after_spark - time_before_spark).total_seconds() 
                self.printd(attributes_log) 
                self.__sql_log(attributes_log)
                return data_frame_spark 
            
        if kwargs.get("refresh"):
            print("[WARNING] The --refresh parameter is only used for adhoc queries.")
        
        if len(re.findall(self.r_drop, query, re.MULTILINE | re.IGNORECASE)) > 0: 
            raise ValueError(f"Is not possible to DROP a DORA's external table")
        
        if re.findall(self.r_user_connections, query, re.MULTILINE | re.IGNORECASE):
            connection = pymysql.connect( host=os.environ['HIVE_BASE'] 
                                        , user=os.environ['HIVE_USER'] 
                                        , password=os.environ['HIVE_PASS'] 
                                        , db='isa', cursorclass=pymysql.cursors.DictCursor) 

            try: 
                with connection.cursor() as cursor: 
                    cursor.execute(f"SELECT connection, jdbc, dialect \
                                   FROM user_connections_v WHERE username='{DORA_USER}'")
                    data = cursor.fetchall()
                    pyspark_df = self.sc.parallelize(data).toDF()
                    return pyspark_df
            finally: 
                connection.close() 
                
        if re.findall(self.r_cache_tables, query, re.MULTILINE | re.IGNORECASE):
            connection = pymysql.connect( host=os.environ['HIVE_BASE'] 
                                        , user=os.environ['HIVE_USER'] 
                                        , password=os.environ['HIVE_PASS'] 
                                        , db='isa', cursorclass=pymysql.cursors.DictCursor) 

            try: 
                with connection.cursor() as cursor: 
                    cursor.execute(f"""SELECT UPPER(CONCAT(s.base,'.',s.catalog_data,'.',s.table)) `table`,
                                   s.cacheDays, s.lastUpdate FROM isa.table_status s
                                   JOIN isa.user_connections_v u on s.base = u.connection 
                                   WHERE s.catalog_data IS NOT NULL AND username = '{DORA_USER}'
                                   ORDER BY 1""")
                    data = cursor.fetchall()
                    pyspark_df = self.sc.parallelize(data).toDF()
                    return pyspark_df
            finally: 
                connection.close() 
 
        if re.findall(self.r_create, query, re.MULTILINE | re.IGNORECASE):
            self.__save_table_query(query)
        
        if re.findall(self.r_d_table, query, re.MULTILINE | re.IGNORECASE):
            connection = pymysql.connect( host=os.environ['HIVE_BASE'] 
                                    , user=os.environ['HIVE_USER'] 
                                    , password=os.environ['HIVE_PASS'] 
                                    , db='isa', cursorclass=pymysql.cursors.DictCursor) 
            try: 

                with connection.cursor() as cursor:
                    table_name = re.search(self.r_d_table, query, re.MULTILINE | re.IGNORECASE).group(1)
                    cursor.execute(f"UPDATE user_tables SET active=0 WHERE table_name='{table_name}'")
                    connection.commit()          
            finally:
                connection.close() 
 
        using_delta=False 
        for n, match in enumerate(re.finditer(self.r_delta, query, re.MULTILINE | re.IGNORECASE), start=1): 
            using_delta=True 
            table_name= self.creat_version_of(match.group(1),match.group(3),match.group(0)) 
            query=query.replace(match.group(0),f" {table_name}") 
        if using_delta: 
            self.printd("delta_query",query) 
        # return True 
        table_list = set([v.group(2) for k,v in enumerate(re.finditer(self.r_select, query, re.MULTILINE | re.IGNORECASE), start=1)]) 
        attributes_log["table_list"] = table_list 
        if len(table_list)>0: 
            self.printd('table_list',table_list) 
        tables_log_meta = self.get_table_status(table_list) 
        table_meta = tables_log_meta[0] 
        table_log = tables_log_meta[1] 
        attributes_log["table_log"] = table_log 
        if len(table_meta)>0: 
            self.printd('table_meta',table_meta) 
        # Lista de execuções submetidas por este sandbox 
        executions = self.load_tables([t for t in table_meta if table_meta[t] is None], table_meta) 
        attributes_log["execution"] = executions 
        # Lista de execuções em andamento por outros sandboxes 
        for execution in [{'executionArn':table_meta[t]['execution']} for t in table_meta if table_meta[t] is not None and table_meta[t].get('status') == 'loading']: 
            executions.append(execution) 
        if len(executions)>0: 
            self.printd('executions',executions) 
        for execution in self.wait_execution(executions): 
            if execution['status']=='FAILED': 
                input_data = json.loads(execution['input']) 
                attributes_log["exist_error"] = f"FAIL to load '{input_data['connection_name']}.{input_data['schema']}.{input_data['table']}'" 
                attributes_log["code_error"] = execution 
                attributes_log["total_time_execution"] = (datetime.datetime.now() - timestamp).total_seconds() 
                self.__sql_log(attributes_log) 
                self.printd(attributes_log) 
                raise ValueError(f"FAIL to load '{input_data['connection_name']}.{input_data['schema']}.{input_data['table']}'") 
        for t in table_meta: 
            if table_meta[t] is None: 
                conn,schema,table=t.split('.') 
                table_id = f"{conn}_{schema}_{table}" 
                query=query.replace(t,f"{CACHE_DB}.{table_id}") 
            else: 
                table_id = f"{CACHE_DB}.{table_meta[t]['table_id']}" 
                query=query.replace(t,table_id) 
 
        self.printd(query) 
        time_before_spark = datetime.datetime.now() 
        data_frame_spark = self.spark.sql(query) 
        time_after_spark = datetime.datetime.now() 
 
        attributes_log["query"] = query 
        attributes_log["total_time_execution"] = (time_after_spark - timestamp).total_seconds() 
        attributes_log["total_time_query"] = (time_after_spark - time_before_spark).total_seconds() 
 
        self.printd(attributes_log) 
        self.__sql_log(attributes_log) 
 
        return data_frame_spark 
 
    def query(self, query, **kwargs):
        """ 
            [WARNING]: This method will be deprecated.
            Faz um wrapper do método sql, alterando alguns parâmetros 
            para manter a compatibilidade com a versão antiga 1.x. 
        
            ---------- 
            query : string 
                Recebe a query bruta. 
            kwargs : dict 
                Argumentos enviados pelo usuário pelo Magic Comand 
            Returns 
            ------- 
            Dataframe 
                retorna o dataframe da query. 
         """
        if kwargs.get("base_name"):
            kwargs["connection"] = kwargs.pop("base_name")
        if kwargs.get("show"):
            return self.sql(query, **kwargs).show()
        return self.sql(query, **kwargs)

        

class ISAMagic(Magics): 
    """
    Jupyter magic command
    """
    from IPython.core.magic import register_cell_magic 
    ipython  = get_ipython() 
    def __init__(self, ISAContext): 
        self.isa = ISAContext 
        self.ipython.register_magic_function(self.sql, 'cell')
        self.ipython.register_magic_function(self.asql, 'cell')
 
    @magic_arguments.magic_arguments() 
    @magic_arguments.argument('--connection', '-c', default=None, help='Connection Name') 
    @magic_arguments.argument('--limit', '-l', type=int, default=100, help='Show limit') 
    @magic_arguments.argument('--verbose', '-v',action='store_true',help='Print Debug messages') 
    @magic_arguments.argument('--out', '-o',help='The variable to return the results in')
    @magic_arguments.argument('--refresh', '-r', help='Refresh cache data', action='store_true')
    def sql(self, line, query): 
        """Execute Spark SQL Query with Dora Engine 
 
        :param query: Spark SQL Query 
 
        :returns: Spark Dataframe 
        :rtype: Dataframe 
 
        Dora Version (2.0) 
        ------- 
        ISA 0.1.4 
        """ 
        args = magic_arguments.parse_argstring(self.sql, line)
        args = vars(args)
        if args.get("out") is None: 
            return self.isa.sql(query,**args).limit(args.get("limit")).toPandas() 
        else: 
            df = self.isa.sql(query,**args) 
            self.ipython.user_ns[args.get("out")] = df 
            return df 
        
    @magic_arguments.magic_arguments() 
    @magic_arguments.argument('--connection', '-c', default=None, help='Connection Name') 
    @magic_arguments.argument('--limit', '-l', type=int, default=100, help='Show limit') 
    @magic_arguments.argument('--verbose', '-v',action='store_true',help='Print Debug messages') 
    @magic_arguments.argument('--out', '-o',help='The variable to return the results in')
    @magic_arguments.argument('--refresh', '-r', help='Refresh cache data', action='store_true')
    def asql(self, line, query): 
        """
        [WARNING]: This method will be deprecated, use sql instead.
        Execute Spark SQL Query with Dora Engine.
    
        :param query: Spark SQL Query 
        
        :returns: Spark Dataframe
        :rtype: Dataframe 
        
        """ 
        args = magic_arguments.parse_argstring(self.sql, line)
        args = vars(args)
        if args.get("out") is None: 
            return self.isa.query(query,**args).limit(args.get("limit")).toPandas()
        else: 
            df = self.isa.query(query,**args) 
            self.ipython.user_ns[args.get("out")] = df 
            return df 
 

# dora=ISAContext(spark)
# asql = ISAContext(spark)
# ISAMagic(dora)
# ISAMagic(asql)
