#!/bin/bash

echo "BUILD START"

# create a virtual environment named 'venv' if it doesn't already exist
python3.12 -m venv env

# activate the virtual environment
source env/bin/activate

# install all deps in the venv
pip install -r requirements.txt

# collect static files using the Python interpreter from venv
python3.12 manage.py collectstatic --noinput

# roda as migrations
python3.12 manage.py migrate

echo "BUILD END"