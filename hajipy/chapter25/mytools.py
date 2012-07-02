#!/usr/bin/env python
# coding: utf-8
class Listner:
  def __repr__(self):
    return ("<Instance of %s, address %s:\n%s>"%
                      (self.__class__.__name__,
                      id(self),
                      self.attrnames()))

  def attrnames(self):
    result = ''
    for attr in self.__dict__.keys():
      if attr[:2] == '__':
        result = result + "\tname %s=<built-in>\n" % attr
      else:
        result = result + "\tname %s=%s\n" % (attr, self.__dict__ [attr])
    return result
        
    

