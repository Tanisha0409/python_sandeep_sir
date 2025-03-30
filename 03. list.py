# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 22:43:58 2025

@author: Dell
"""

#list 

l = [10,20,30,40,50]

print(l)
print(l[3])
print(l[-1])
print(l[-2])

#list insert and search function
l.append(30)
print(l)
l.insert(1,15)
print(l)
print(15 in l)
print(l.count(30))
print(l.index(30))

#removal of item from list
l1 = [10,20,30,40,50,60,70,80]
l1.remove(20)
print(l1)
print(l1.pop())
print(l1)
print(l1.pop(2))
print(l1)
del l1[1]
print(l1)
del l1 [0:2]
print(l1)

#general function 
l2 = [10,40,20,50]
print(max(l2))
print(min(l2))
print(sum(l2))
l2.reverse()
print(l2)
l2.sort()
print(l2)