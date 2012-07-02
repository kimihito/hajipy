#!/usr/bin/env python
# coding: utf-8
class PrivateExc(Exception): pass

class Privacy:
  def __setattr__(self, attrname, value):
    if attrname in self.privates:
      raise PrivateExc(attrname, self)
    else:
      self.__dict__[attrname] = value

class Test1(Privacy):
  privates = ['age']

class Test2(Privacy):
  privates = ['name','pay']
  def __init__(self):
    self.__dict__['name'] = 'Tom'

x = Test1()
y = Test2()

x.name = 'Bob'
y.name = 'Sue'

y.age = 30
x.age = 40

