#!/usr/bin/env python
# coding: utf-8
class C1(C2,C3):
  def setname(self, who):
    self.name = who

L1 = C1()
L2iL2 = C1()
L1.setname('bob')
L2.setname('mel')
print L1.name
