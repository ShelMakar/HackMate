#!/bin/sh

set -e

cd /app/hackmate

python manage.py migrate --noinput

exec "$@"