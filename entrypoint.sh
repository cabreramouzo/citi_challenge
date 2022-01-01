#!/bin/sh

cd ./citibeats_challenge

python manage.py collectstatic --noinput -link
python manage.py migrate --noinput

gunicorn citibeats_challenge.wsgi:application -b 0.0.0.0:8080 --timeout 120 --access-logfile -