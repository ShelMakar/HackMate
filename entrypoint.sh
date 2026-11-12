#!/bin/sh

set -e

cd /app/hackmate

mkdir -p data

python manage.py migrate --noinput

exec "$@"