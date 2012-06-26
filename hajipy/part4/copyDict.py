#!/usr/bin/env python
# coding: utf-8
def copyDict(arg):
  new = {}
  for key in arg.keys():
    new[key] = arg[key]

  print new

copyDict({'a':1,'b':2})
copyDict({'a':3,'b':2,'c':3})
copyDict({'a':1,'b':2, 'c':3,'d':4})
