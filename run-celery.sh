#!/usr/bin/env bash

BASEDIR=$(dirname $0)
VENV=/venv/bin/activate

LIBAPP=libapp
CELERY=subscriber.celeryd

CONFIG=/libapp/config/libconf.py

QUEUE=celery
while IFS='' read -r line || [[ -n "$line" ]]; do
    IFS='=' read -a array <<< "$line"
    echo ${array[0]}
    Q_TYPE="$(echo -e "${array[0]}" | sed -e 's/^[[:space:]]*//')"
    if [ "${Q_TYPE}" == "EMAIL_Q" ]; then
        QUEUE=${array[1]}

        QUEUE="${QUEUE%\"}"
        QUEUE="${QUEUE#\"}"
    fi
done < $BASEDIR$CONFIG

source $BASEDIR$VENV
celery -A $LIBAPP.$CELERY worker -Q $QUEUE --loglevel=info --concurrency=1
