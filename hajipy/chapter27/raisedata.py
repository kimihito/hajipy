#!/usr/bin/env python
# coding: utf-8
myException = 'Error'

def raiser1():
  raise myException, "hello"

def raiser2():
  raise myException

def tryer(func):
  try:
    func()
  except myException, extraInfo:
    print 'got this:', extraInfo
