#!/bin/sh 
yes | python manage.py makemigrations --settings=Gotalk.settings

echo "==> Django setup, executing: migrate pro"
python manage.py migrate --settings=Gotalk.settings --fake-initial

echo "==> Django setup, executing: collectstatic"
python manage.py collectstatic --settings=Gotalk.settings --noinput -v 3

pip install -r /srv/code/requirements.txt
echo "==> Django deploy"

daphne -b 0.0.0.0 -p 8000 Gotalk.asgi:application
#gunicorn -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=Gotalk.settings Gotalk.wsgi:application