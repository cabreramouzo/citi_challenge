#!/bin/bash

cd ./citibeats_challenge

python manage.py collectstatic --noinput -link
python manage.py migrate --noinput

EXPOSED_PORT=${PORT}
if [ "${EXPOSED_PORT}" = "" ]; then
  EXPOSED_PORT="8080"
fi

if [ "${DJANGO_SUPERUSER_EMAIL}" != "" ]; then
  python manage.py createsuperuser --email "${DJANGO_SUPERUSER_EMAIL}" --noinput
fi

gunicorn citibeats_challenge.wsgi:application -b 0.0.0.0:${EXPOSED_PORT} --access-logfile -