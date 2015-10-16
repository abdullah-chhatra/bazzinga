#!/usr/bin/env bash
#TEST=True
#export TEST

BASEDIR=$(dirname $0)
VENV=/venv/bin/activate

source $BASEDIR$VENV
python manage.py runserver