#!/usr/bin/env python
# coding: utf-8
X = 11

def f():
  print X

def g():
  X = 22
  print X

class C:
  X = 33
  def m(self):
    X = 44
    self.X = 55

if __name__ == '__main__':
  print X
  f()
  g()
  print X

  obj = C()
  print obj.X

  obj.m()
  print obj.X
  print C.X

  #print c.m.X
  #print f.X
