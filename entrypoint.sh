#!/bin/sh

cd ./citibeats_challenge

python manage.py collectstatic --noinput -link
python manage.py migrate --noinput
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell

gunicorn citibeats_challenge.wsgi:application -b 0.0.0.0:8080 --access-logfile -