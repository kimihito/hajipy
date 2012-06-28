#!/usr/bin/env python
# coding: utf-8
class C1(C2,C3):
  def __init__(self, who):
    self.name = who

L1 = C1('bob')
L2 = C1('mel')
print L1.name
