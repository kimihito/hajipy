#!/usr/bin/env python
# coding: utf-8
def printNumInstances():
    print "Number of instances created: ", Spam.numInstances
class Spam:
  numInstances = 0
  def __init__(self):
    Spam.numInstances = Spam.numInstances + 1
