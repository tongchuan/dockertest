#!/usr/bin/python3
#coding=utf-8

class Config(object):
  # ENV='development' # 'production'
  DEBUG=True
  # TESTING=True
  # PROPAGATE_EXCEPTIONS=True
  # PRESERVE_CONTEXT_ON_EXCEPTION=True
  # TRAP_HTTP_EXCEPTIONS=True
  # TRAP_BAD_REQUEST_ERRORS=None
  # SECRET_KEY='abcdefghijklmnopkuxyzw'
  # SESSION_COOKIE_NAME='session'
  # SESSION_COOKIE_DOMAIN=None
  # SESSION_COOKIE_PATH='/'
  # SESSION_COOKIE_HTTPONLY=True
  # SESSION_COOKIE_SECURE=False
  # SESSION_COOKIE_SAMESITE=None
  # PERMANENT_SESSION_LIFETIME=timedelta(days=31)
  # SESSION_REFRESH_EACH_REQUEST=True
  # USE_X_SENDFILE=False
  # SERVER_NAME=None
  # APPLICATION_ROOT='/'
  # PREFERRED_URL_SCHEME='http'
  # MAX_CONTENT_LENGTH=None
  # JSON_AS_ASCII=True
  # JSON_SORT_KEYS=True
  # JSONIFY_PRETTYPRINT_REGULAR=False
  # JSONIFY_MIMETYPE='application/json'
  # TEMPLATES_AUTO_RELOAD=None
  # EXPLAIN_TEMPLATE_LOADING=False
  # MAX_COOKIE_SIZE=4093
  HOST='0.0.0.0'
  PROT='5000'
  DB_SERVER = '192.168.1.56'
  # SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@10.6.223.177:3306/mypython?charset=utf8'
  # CREATE DATABASE mypython CHARSET=UTF8;
  SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@172.18.0.3:3306/mypython?charset=utf8'
  
  # SQLALCHEMY_DATABASE_URI="mysql://root:root@127.0.0.1:3306/mydata"
  SQLALCHEMY_COMMIT_ON_TEARDOWN=True
  SQLALCHEMY_TRACK_MODIFICATIONS=True
  # SQLALCHEMY_TRACK_MODIFICATIONS
  # @property
  # def DATABASE_URI(self):         # Note: all caps
  #   return 'mysql://user@{}/foo'.format(self.DB_SERVER)

class ProductionConfig(Config):
  DEBUG=False
  Zhang="kaishi"

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True