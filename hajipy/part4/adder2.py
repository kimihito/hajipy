#!/usr/bin/env python
# coding: utf-8
def adder(*args):
  result = args[0]
  for arg in args:
    result += arg[1:]
  print result 
  

adder({'a':1, 'b':2},{'c':3,'d':4})
adder("aaa","BBB","cccc")
adder([1,2,3],[4,5,6])


