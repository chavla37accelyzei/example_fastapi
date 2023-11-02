#!/bin/sh

cd /emp-erp
pip3 install -r requirements.txt

python create_tables.py

# python3 manage.py migrate

exec "$@"

