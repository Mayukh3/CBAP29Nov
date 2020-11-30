#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:05:52 2020

@author: mayukhchakraborty
"""

# List, Tupple, Dictionary, Frozen Set

L1 = []
L1 = [10, 20, 30, 40, 50]

L2= [10, 20.7, "Vikas", True]

print(L2)

print(L2[4])

L2[1] = 30.5
L2

L2[1]= 'Hello'
L2

for i in L2:
    print(i)
    print("inside the loop")
    
    print("outside the loop")
    

r1 = range(5,10)
print(r1)
lr2 = list(r1)
lr2

r3 = range(0, 10, 3)
print(r3)
lr3 = list(r3)
print(lr3)


for i in lr3:
    print(i)
    
len(lr3)

for i in range(0,10):
    
    

for i in range(len(lr3)):
    print(i*2)
    
    
L4= [1,2,3, 'vikas', True, 'vikas', 'vikas']

L4[3]=L4[3].capitalize()

L4

print (L4.count('vikas'))


L5= [1,2,3,4]
print(L5)

L5[4]=20

L5.append(7)
L5

L5.append('Vikas')
L5

L5.append([8,'vikas'])
L5


L5.remove(2)
L5

print(L5.remove(3))


s = "Vikas"

print(s.upper().capitalize())



L5 = [1,2,3,4]

print(L5.pop())
L5
print(L5.pop(1))
L5
L5 = [1,2,3,4]
L5.clear()
L5


del L5
L5



L1 = [1,2,'Vikas','Khullar',True]
L1
L2=L1
L2

L1.append(5)

L1
L2





L5.clear()
L5


L3=L1.copy()
L1
L3
L1.append(11)
L1
L3



L5=[1,2,3,4]

L6=L5[0:2]

L6

L5[1]=88
L6


