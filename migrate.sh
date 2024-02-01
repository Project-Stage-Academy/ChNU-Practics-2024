#!/usr/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"hello@tkachuk.email"}

cd /app/

PIP_BIN=/app/venv/bin/pip

$PIP_BIN manage.py migrate --noinput
$PIP_BIN createsuperuser --email $SUPERUSER_EMAIL --noinput || true
