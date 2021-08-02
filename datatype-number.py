#python datatypes
import  math
"""
1. Number(int,float,complex)
2.string
3.list
4.tuple
5.dictionary
6.sets
7.boolean
"""

#array datatype is not in python

""" NUMBER TYPE (INT,FLOAT,COMPLEX) """

a=int(12)
print(type(a))

#Some Math Function

""" The abs() function returns the absolute value of the specified number."""
#Required. A number
#Example


print(abs(-4.00))
print(abs(-0.3+8))

#MIN

print (min(12,46,78))


#MAX

print (max(23,66,88))

#pow

print(pow(3,4))

#round
print(round(8.68))

#cmp
"""a and b are the two numbers in which the comparison is being done.cmp() method in Python 2.x compares two integers and returns -1, 0, 1 according to comparison.
cmp() does not work in python 3.x. 
print(cmp(1,2))
# use of cmp() method
  
# when a<b
a = 1 
b = 2 
print(cmp(a, b))  
  
# when a = b 
a = 2
b = 2 
print(cmp(a, b))  
  
# when a>b 
a = 3
b = 2 
print(cmp(a, b))"""


### Random Range

import random
from random import randint, randrange

seq=[1,3,6,9,8,9,0]
print(type(seq))
# Randomly select one number in seq
print(random.choice(seq))

#random rand 

print(random.random())

#random rand range 6 digit

print(random.randrange(1,600000))

#random uniform

print(random.uniform(4,6))

#random seed

random.seed(10)
print(random.random())
