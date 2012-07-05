#!/usr/bin/env python
# coding: utf-8
class Adder:
  def __init__(self, data=[]):
    self.data = data
  def __add__(self, y):
    return self.add(self.data, y)

  def add(self, x, y):
    print 'Not Implemented'

class ListAdder(Adder):
  def add(self, y):
    return self.data  + y

class DictAdder(Adder):
  def add(self, y):
    x = self.data
    x.update(y)
    return x

if __name__ == '__main__':
  a = Adder()
  print a.add(1,2)
  b = ListAdder()
  print   b.add("aaa", "bbb")
  c = DictAdder()
  print c.add({'a':1, 'b':2}, {'a':1, 'c':2},)
