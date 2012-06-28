#!/usr/bin/env python
# coding: utf-8
import sys

def countLines(name):
  f = open(name)
  lines = f.readline()
  return len(lines)

def countChars(name):
  f = open(name)
  return len(f.read())

def test(name):
#  print countLines(name)
#  print countChars(name)

  return countLines(name), countChars(name)

if __name__ == '__main__':
  print 'Please Type file name:'
  x = raw_input()
  test(x)
