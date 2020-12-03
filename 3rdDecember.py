#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:05:08 2020

@author: mayukhchakraborty
"""

import numpy as np

np.random.randint(100, 1000)

x1 = np.random.randint(100, 200, size=10)

x1

x1.shape

x2= np.random.randint(100, 200, size = (3,4))

x2

x2.shape

x1[0]

x1[2]

x1[1:5]
x1[::]


x3= np.random.randint(100, 200, size= (2,3,4))

x3.shape

x1

x1[1:4]

x1[::2]

x4=np.random.randint(10,20,size=(5,5))
x4


x4[2,2]
x4[2,4]
x4[4,2]
x4[5,2]

x4[0,:]

x4[:,0]





x4[:2,:2]

x4[:2,-2:]



x4[::2,:]
x4[:,::2]



ar1=np.arange(20)

ar1

ar2=np.arange(10,20)
ar2

ar3=np.arange(10,20, step=2)
ar3

x4
x4.shape

t1=(5,5)
t1
t1[0]
t1[1]


for i in range(x4.shape[0]):
    for j in range(x4.)



x5 = np.arange(0,20)
x5

x5.shape

x5.reshape(3.7)



a = np.zeros((2,4))
a

b=np.ones((4,2))
b



c=np.eye(3,3)

ls1=np.linspace(1,15, num=4)
ls1


x6=np.array([(1,2,3),(5,6,7)])


x7=np.array([1,2,3])

x7




x8=np.array([1,2,3],dtype='int')
x8


x9=np.random.randint(40,100,size=10000000)
x9

np.min(x9)
np.max(x9)
np.mean(x9)
np.median(x9)

nl1=np.linspace(0,10,5)
nl1

np.diff(nl1)
np.round(nl1)
np.floor(nl1)
np.ceil(nl1)


np.round([1.2])











x4=np.array([1,2,3,4,5,6])
x4
x5=np.ones(10)
x5

np.concatenate([x4,x5])



x4=x4.reshape(3,2)
x4.shape


np.concatenate([x4,x5], axis=0)

x5

np.vstack([x4,x5])



x7=np.arange(10)


np.add(x4,x4)
np.multiply(x4,x4)

x8=np.random.randint(5,100,size=(5,5))
x8

np.mean(x8)
np.mean(x8,axis=1)
np.mean(x8,axis=0)

np.sum(x8)
np.sum(x8, axis=1)



np.equal(x8,52)


np.greater(x8,52)



np.all(x8>40)

x9= np.sort(x8)
x9

x8

x10=np.sort(x8, axis=0)
x10


x=np.arange(1,13).reshape(3,4)
x
x.T


from matplotlib import pyplot as plt
import numpy as np

n_arr=np.random.normal(100,20,1000)
n_arr

l1=list(range(50,150))

plt.hist(n_arr, bins =l1)
plt.title("histogram")


n_arr

np.mean(n_arr)
np.std(n_arr)



