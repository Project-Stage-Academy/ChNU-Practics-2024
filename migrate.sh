#!/usr/bin/sh
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@example.com"}

set -e

cd /app/

sleep 5

PYTHON_BIN=/opt/venv/bin/python

$PYTHON_BIN src/manage.py collectstatic --noinput

$PYTHON_BIN src/manage.py migrate --noinput
$PYTHON_BIN src/manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
