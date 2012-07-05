#!/usr/bin/env python
# coding: utf-8
def action2():
  print 1 + []

def action1():
  try:
    action2()
  except TypeError:
    print 'inner try'

try:
  action1()
except TypeError:
  print 'outer try'
