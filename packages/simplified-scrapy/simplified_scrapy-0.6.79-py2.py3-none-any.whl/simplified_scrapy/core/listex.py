#!/usr/bin/python
#coding=utf-8
class List(list):
  def contains(self, value, attr='html'):
    tmp=[]
    for l in self:
      if hasattr(l, 'contains'):
        flag = l.contains(value,attr)
        if not flag: tmp.append(l)
    for t in tmp:
      self.remove(t)
    return self

  def notContains(self, value, attr='html'):
    tmp=[]
    for l in self:
      if hasattr(l, 'notContains'):
        flag = l.notContains(value,attr)
        if not flag: tmp.append(l)
    for t in tmp:
      self.remove(t)
    return self

  def containsReg(self, value, attr='html'):
    tmp=[]
    for l in self:
      if hasattr(l, 'containsReg'):
        flag = l.containsReg(value,attr)
        if not flag: tmp.append(l)
    for t in tmp:
      self.remove(t)
    return self

  
