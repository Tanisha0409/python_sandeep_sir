# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 22:26:42 2025

@author: Dell
"""

#id()

a = 10
b = 10
print(id(a))
print(id(b))


#is operator

a = 10
b = 10
print(a is b)

c = a
print(c is b)

c = 20
print(c is b)

#type function

a = 10
print(type(a))

b = 10.5
print(type(b))

c = 2+4j
print(type(c))

d = True
print(type(d))

e = None
print(type(e))


s = "gfg"
print(type(s))

l = [10,20,30]
print(type(l))

t = (10,20,30)
print(type(t))

set_1 = {2,3,4,2,3}
print(type(set_1))

d = {10:"gfg", 20:"ide"}
print(type(d))
