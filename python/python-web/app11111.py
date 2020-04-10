#!/usr/bin/python
# coding=utf-8
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!1"

@app.route('/main')
def main():
  return "my name is main222"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)