#!/usr/bin/env bash
set -e

POSTGRES_HOST=${POSTGRES_HOST:-"localhost"}
POSTGRES_PORT=${POSTGRES_PORT:-"5432"}

sleep 2 # wait for postgres to start

[ -d /app/ ] && cd /app/

PYTHON_BIN="/opt/venv/bin/python"
[ ! -f "$PYTHON_BIN" ] && PYTHON_BIN="python"

# Run migrations and create superuser
$PYTHON_BIN src/manage.py makemigrations --noinput
$PYTHON_BIN src/manage.py migrate --noinput

SUPERUSER_EXISTS=$($PYTHON_BIN src/manage.py shell -c "
import os
from dotenv import load_dotenv
from apps.users.models import User

load_dotenv()
print(User.objects.filter(email=os.getenv('DJANGO_SUPERUSER_EMAIL')).exists())
")

[ "$SUPERUSER_EXISTS" != "True" ] && $PYTHON_BIN src/manage.py createsuperuser --noinput || true
