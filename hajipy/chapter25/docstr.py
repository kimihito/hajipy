#!/usr/bin/env python
# coding: utf-8
"I am: docstr.__doc__"

class spam:
  "I am: spam.__doc__ or docstr.spam.__doc__"

  def method(self, arg):
    "I am: spam.method.__doc__ or self.method.__doc__"
    pass

  def func(args):
    "I am: docstr.func.__doc__"
    pass
