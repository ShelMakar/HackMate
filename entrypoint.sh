#!/bin/sh
set -e

python hackmate/manage.py migrate --noinput

exec "$@"