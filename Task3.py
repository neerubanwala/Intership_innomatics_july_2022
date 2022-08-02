#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PolarCoordinates
from cmath import *

z = input()

print(abs(complex(z)))
print(phase(complex(z)))


# In[ ]:


#FindAngleMBC
import math
ab=int(input())
bc=int(input())
ca=math.hypot(ab,bc)
mc=ca/2
bca=math.asin(1*ab/ca)
bm=math.sqrt((bc**2+mc**2)-(2*bc*mc*math.cos(bca)))
mbc=math.asin(math.sin(bca)*mc/bm)
print(int(round(math.degrees(mbc),0)),'\u00B0',sep='')


# In[ ]:


#TriangleQuest2
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (((10**i - 1)//9)**2)


# In[ ]:


#ModDivmod
print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))


# In[ ]:


#ModPower
a,b,m = [int(input()) for _ in '123']
print(pow(a,b),pow(a,b,m),sep='\n')


# In[ ]:


#IntegersComeInAllSizes
a,b,c,d = (int(input()) for _ in range(4))
print (pow(a,b)+pow(c,d))


# In[ ]:


#TriangleQuest
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**(i)//9)*i)

