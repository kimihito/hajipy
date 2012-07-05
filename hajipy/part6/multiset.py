#!/usr/bin/env python
# coding: utf-8
from setwrapper import Set

class MultiSet(Set):
  def intersect(self, *others):
    res = []
  for x in self:
    for other in others:
      if x not in other: break
    else:
      res.append(x)
  return Set(res)

  def union(*args):
    res = []
    for seq in args:
      for x in seq:
        if not x in res:
          res.append(x)
    return Set(res)
  
