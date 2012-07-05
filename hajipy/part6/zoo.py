#!/usr/bin/env python
# coding: utf-8
class Animal:
  def reply(self): self.speak()
  def speak(self): print 'spam'

class Mammal(Animal):
  def speak(self): print 'huh?'

class Cat(Mammal):
  def speak(self): print 'meow'

class Dog(Mammal):
  def speak(self): print 'bark'

class Primate(Mammal):
  def speak(self): print 'Hello, World!'

class Hacker(Primate): pass
