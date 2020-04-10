#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
mkdir mypython
cd mypython
sudo apt-get install python-virtualenv
sudo apt-get install python3-pip
virtualenv -p /usr/bin/python3 venv
 virtualenv --no-site-packages venv
source ./venv/bin/activate
./venv/bipip3 install uwsgi
./venv/bin/uwsgi --http :8000 --gi-file test.py 

sudo pip3 install Django==2.0.3
django-admin startproject myweb

uwsgi --http :8000 --chdir /home/setup/myweb --wsgi-file myweb/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:8001
'''
import sys
print(sys.version)

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b'Hello World']