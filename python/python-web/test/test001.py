#!/usr/bin/python3
#coding=utf-8
import os
from ztc import zhang

print(os.name)
try:
  pass
except ValueError as e:
  pass
except ZeroDivisionError as e:
  pass
except UnicodeError as e:
  pass
finally:
  pass
if __name__ == '__main__':
  print(dir(zhang.kaishi))