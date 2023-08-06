#!/usr/bin/python
#coding=utf-8
class List(list):
  def contains(self, value):
    tmp=[]
    for l in self:
      if hasattr(l, 'contains'):
        flag = l.contains(value)
        if not flag: tmp.append(l)
    for t in tmp:
      self.remove(t)
    return self

  def notContains(self, value):
    tmp=[]
    for l in self:
      if hasattr(l, 'notContains'):
        flag = l.notContains(value)
        if not flag: tmp.append(l)
    for t in tmp:
      self.remove(t)
    return self

  def containsReg(self, value):
    tmp=[]
    for l in self:
      if hasattr(l, 'containsReg'):
        flag = l.containsReg(value)
        if not flag: tmp.append(l)
    for t in tmp:
      self.remove(t)
    return self

  
