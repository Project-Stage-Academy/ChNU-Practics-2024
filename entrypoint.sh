#!/usr/bin/sh
APP_PORT=${PORT:-8080}

set -e

cd /app

/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm config.wsgi:application --bind "0.0.0.0:${APP_PORT}"
