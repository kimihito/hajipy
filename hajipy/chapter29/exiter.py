#!/usr/bin/env python
# coding: utf-8
import sys

def bye():
  sys.exit(40)

try:
  bye()
except:
  print 'go it'
print 'continuing...'
