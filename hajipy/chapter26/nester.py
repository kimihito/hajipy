#!/usr/bin/env python
# coding: utf-8
def generate():
  class Spam:
    count = 1
    def method(self):
      print Spam.count
  return Spam()

generate().method()
