#!/usr/bin/env python
# coding: utf-8
def minmax(test, *args):
  res = args[0]
  for arg in args[1:]:
    if test(arg, res):
      res = arg

  return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

print minmax(lessthan,4,3,2,2,4,6,5)
print minmax(grtrthan,4,3,2,2,4,6,5)

