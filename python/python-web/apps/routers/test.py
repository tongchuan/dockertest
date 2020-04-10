#!/usr/bin/python3
#coding=utf-8
from flask import Blueprint,render_template

testIndex=Blueprint('test_index',__name__)

@testIndex.route('/test')
def test_index():
  return 'abc'