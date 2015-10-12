#!/usr/bin/env bash
source ./venv/bin/activate
celery -A junk.email_task.celery worker --loglevel=info --concurrency=1
