#!/usr/bin/env bash
set -e

POSTGRES_HOST=${POSTGRES_HOST:-"localhost"}
POSTGRES_PORT=${POSTGRES_PORT:-"5432"}

cd /app/

sleep 2 # wait for postgres to start

PYTHON_BIN=/opt/venv/bin/python

$PYTHON_BIN src/manage.py makemigrations --noinput
$PYTHON_BIN src/manage.py migrate --noinput

$PYTHON_BIN src/manage.py createsuperuser --noinput || true
