#!/usr/bin/env python
# coding: utf-8
from mytools import Listner

class Super:
  def __init__(self):
    self.data1 = "spam"

class Sub(Super, Listner):
  def __init__(self):
    Super.__init__(self)
    self.data2 = "eggs"
    self.data3 = 43

if __name__ == '__main__':
  X = Sub()
  print X
