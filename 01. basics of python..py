# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 22:08:24 2025

@author: Dell
"""

#python basics

print("hello world!")

#comment

'''
doc string 1
'''

"""
doc string 2

"""

#variable
age = 38
name = "ankit"
weight = 58.5

print(age)
print(name)
print(weight)


price = 100
tax = 18
total_price = price + tax
print(total_price)


x = 10
y = 'geek'
z = 20
w = z
w = 30
print(x,y,z,w)


x = 10
print(x)
x = "geek"
print(x)


is_valid = True
mark = 90
pi = 3.14
city_name = "noida"
print(is_valid)
print(mark)
print(pi)
print(city_name)



'''
using a variable without assigning it causes error
'''
print(x)

#special value 'none'
x = "none"
print(x)

'''
swap two variable using extra variable
input: x ="geeks", y ="for"
output: x ="for", y ="geeks"
'''
x = "geeks"
y = "for"
z = x
x = y
y = z

print(x)
print(y)



x = 100
y = 20
#output: x=20, y=100

z=x
x=y
y=z

print(x)
print(y)

'''
swap variable using comma assignment
'''
x = 100
y = 200

x,y = y,x
print(x)
print(y)




x, y, z = 100, "geeks", 10.5
print(x,y,z)

x, y = x-5, y+"for"

print(x)
print(y)
print(z)