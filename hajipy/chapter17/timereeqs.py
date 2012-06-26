#!/usr/bin/env python
# coding: utf-8
import time, sys
reps = 1000
size = 10000

def tester(func, *args):
  startTime = time.time()
  for i in range(reps):
    func(*args)
  elapsed = time.time() - startTime
  return elapsed

def forStatement():
  res = []
  for x in range(size):
    res.append(x + 10)

def listComprehension():
  res = [x + 10 for x in range(size)]

def mapFunction():
  res = map((lambda x: x +10), range(size))

def generatorExpression():
  res = list(x + 10 for x in range(size))

print sys.version
tests = (forStatement, listComprehension, mapFunction, generatorExpression)
for testfunc in tests:
  print testfunc.__name__.ljust(20), '=>', tester(testfunc)


