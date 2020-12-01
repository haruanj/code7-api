#!/bin/sh

pip install -r requirements.txt


python .dev/scripts/create_mongo_user.py

python manage.py runserver 0.0.0.0:8000
