#!/usr/bin/env python
# coding: utf-8
class Number:
  def __init__(self, start):
    self.data = start
  def __sub__(self,other):
    return Number(self.data - other)
