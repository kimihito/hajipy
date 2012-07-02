#!/usr/bin/env python
# coding: utf-8
from streams import Processor

class Uppercase(Processor):
  def converter(self,data):
    return data.upper()

if __name__ == '__main__':
  import sys
  Uppercase(open('spam.txt'), sys.stdout).process()
