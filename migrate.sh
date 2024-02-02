#!/usr/bin/sh
set -e

cd /app/

sleep 5

PYTHON_BIN=/opt/venv/bin/python

$PYTHON_BIN src/manage.py collectstatic --noinput

$PYTHON_BIN src/manage.py migrate --noinput
$PYTHON_BIN src/manage.py createsuperuser --noinput || true
