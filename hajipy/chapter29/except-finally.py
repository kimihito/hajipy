#!/usr/bin/env python
# coding: utf-8
def raise1(): raise IndexError
def noraise():  return
def raise2(): SyntaxError

for func in (raise1, noraise, raise2):
  print '\n'
  try:
    try:
      func()
    except IndexError:
      print 'caught IndexError'
  finally:
    print 'finally run'
