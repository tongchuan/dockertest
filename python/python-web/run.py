#!/usr/bin/python3
#coding=utf-8
from apps import app
# app.config.update(DEBUG=app.config['DEBUG']) 
# app.config.update(HOST=app.config['HOST']) 
if __name__ == '__main__':
  app.run(host=app.config['HOST'],port=app.config['PROT'],debug=app.config['DEBUG'])
# static_url_path