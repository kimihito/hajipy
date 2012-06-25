#!/usr/bin/env python
# coding: utf-8
def intersect(*args):
  res = []
  for x in args[0]:
    for other in args[1:]:
      if x not in other: break
    else:
      res.append(x)
  return res

def union(*args):
  res = []
  for seq in args:
    for x in seq:
      if x not in res:
        res.append(x)
  return res

