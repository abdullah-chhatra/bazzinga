#!/usr/bin/env bash

BASEDIR=$(dirname $0)
VENV=/venv/bin/activate

LIBAPP=libapp
CELERY=email_task.celeryd

source $BASEDIR$VENV
celery -A $LIBAPP.$CELERY worker --loglevel=info --concurrency=1
