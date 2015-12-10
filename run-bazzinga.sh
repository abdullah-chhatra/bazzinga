#!/bin/bash
#TEST=True
#export TEST

BASEDIR=$(dirname $(readlink -f $0))
VENV=/venv/bin/activate

source $BASEDIR$VENV
python $BASEDIR/manage.py runserver