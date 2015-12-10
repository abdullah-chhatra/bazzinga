#!/usr/bin/env bash
#TEST=True
#export TEST

#BASEDIR=$(dirname $0)
BASEDIR=$(dirname $(readlink -f $0))
VENV=/venv/bin/activate

source $BASEDIR$VENV
python $BASEDIR/manage.py runserver