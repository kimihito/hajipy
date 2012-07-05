#!/usr/bin/env python
# coding: utf-8
General = 'general'
Specific1 = 'specific1'
Specific2 = 'specific2'

def raiser0():  raise General
def raiser1():  raise Specific1
def raiser2():  raise Specific2

for func in (raiser0, raiser1, raiser2):
  try:
    func()
  except (General, Specific1, Specific2):
    import sys
    print 'caught:', sys.exc_info()[0]

