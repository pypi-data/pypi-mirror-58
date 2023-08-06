#!/bin/bash

if [[ "$(curl -o -I -L -s -w '%{http_code}'  'http://169.254.169.254/latest/meta-data/public-hostname')" -ne 200 ]] ; then
    export DORA_HOST=$(curl -sL "http://169.254.169.254/latest/meta-data/local-ipv4")
else
    export DORA_HOST=$(curl -sL "http://169.254.169.254/latest/meta-data/public-hostname")
fi

export DORA_INSTANCE=$(curl -sL "http://169.254.169.254/latest/meta-data/instance-id")

if [[ -z "$DORA_HOST" ]]; then
   export DORA_HOST=localhost
fi

export SPARK_MASTER_PORT=7077

export DORA_SPARK="spark://`hostname`:$SPARK_MASTER_PORT"
export timestamp=$(date +%Y-%m-%d_%H-%M-%S)

$SPARK_HOME/sbin/start-master.sh 1> ${DORA_DATA}/logs/master_${timestamp}.log 2> ${DORA_DATA}/logs/master_${timestamp}.error
$SPARK_HOME/sbin/start-slave.sh --memory "${DORA_MEM}" $DORA_SPARK 1> ${DORA_DATA}/logs/slave_${timestamp}.log 2> ${DORA_DATA}/logs/slave_${timestamp}.error
spark-submit --executor-memory "${DORA_MEM}" --driver-memory "${DORA_MEM}" --conf spark.sql.catalogImplementation=hive --master ${DORA_SPARK} /etc/ml/score/init.py "$@" 2> ${DORA_DATA}/logs/score_${timestamp}.log

echo "Container Id of ML Code Execution: $(cat /etc/hostname)"

echo "To copy the generated data run: docker cp $(cat /etc/hostname):/data . "