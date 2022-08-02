#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#SwapCase
def swap_case(s):
    return s.swapcase()


# In[ ]:


#StringSplit&Join
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line


# In[ ]:


#What'sYourName?
def print_full_name(a,b):
    print("Hello {} {}! You just delved into python.".format(a,b))


# In[ ]:


#Mutations
def mutate_string(string, position, character):
    n = list(string)
    n[position] = character
    string = "".join(n)
    return string


# In[ ]:


#FindAString
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)-len(sub_string)+1):
        l = i
        for j in range(0, len(sub_string)):
            if string[l] == sub_string[j]:
                l +=1
                if j == len(sub_string)-1:
                    count = count + 1
                else:
                    continue
            else:
                break
            
    return count


# In[ ]:


#StringValidators
if __name__ == '__main__':
    s = input()
    print(any(a.isalnum() for a in s) )
    print(any(a.isalpha() for a in s) )
    print(any(a.isdigit() for a in s) )
    print(any(a.islower() for a in s) )
    print(any(a.isupper() for a in s) )


# In[ ]:


#TextAllignments
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))  
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[ ]:


#TextWrap
import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    dedented_text = textwrap.dedent(text=string) 
    result = wrapper.fill(text=dedented_text) 
    return result


# In[ ]:


#DesignerDoorMat
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


# In[ ]:


#StringFormatting
def print_formatted(number):

    width = len("{0:b}".format(number))

    for i in range(1, number + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# In[ ]:


#AlphabetRangoli
def print_rangoli(size):
    # your code goes here
    import string
    design = string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# In[ ]:


#Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

if __name__ == '__main__':


# In[ ]:


#TheMinionGame
def minion_game(string):
    vowels = 'AEIOU'
    Stuart_score, Kevin_score = 0, 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    if Stuart_score < Kevin_score:
        print('Kevin {}'.format(Kevin_score))


# In[ ]:


#MergeTheTools
def merge_the_tools(string, k):
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

