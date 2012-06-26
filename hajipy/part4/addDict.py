#!/usr/bin/env python
# coding: utf-8
def addDict(d1, d2):
  new = {}
  for key in d1.keys():
    new[key] = d1[key]
  for key in d2.keys():
    new[key] = d2[key]
  print new

addDict({'a':1,'b': 2}, {'a':1,'b':2}) 
addDict({'a':1,'b': 2}, {'d':1,'e':2}) 
addDict({'a':1,'b': 2}, {'a':5,'f':88888888}) 
