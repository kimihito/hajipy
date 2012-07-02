#!/usr/bin/env python
# coding: utf-8
class SkipIterator:
  def __init__(self, wrapped):
    self.wrapped = wrapped
    self.offset = 0
  def next(self):
    if self.offset >= len(self.wrapped):
      raise StopIteration
    else:
      item = self.wrapped[self.offset]
      self.offset += 2
      return item

class SkipObject:
  def __init__(self,wrapped):
    self.wrapped = wrapped
  def __iter__(self):
    return SkipIterator(self.wrapped)

if __name__ == '__main__':
  alpha = 'abcdef'
  skipper = SkipObject(alpha)
  I = iter(skipper)
  print I.next(), I.next(), I.next()

  for x in skipper:
    for y in skipper:
      print x + y,
