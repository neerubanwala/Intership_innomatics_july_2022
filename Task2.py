#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ListComprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = [];
    abc = [];
    for X in range (x+1):
        for Y in range (y+1):
            for Z in range (z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z];
                    output.append(abc);
print(output);  


# In[ ]:


#Runner-upScore
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])


# In[ ]:


#Nestedlists
if __name__ == '__main__':
    students =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    x = 99999
    for i in range (len(students)):
        if x>float(students[i][1]):
            x = float(students[i][1])
    y = 999999   
    for i in range(len(students)):
        if float(students[i][1])>float(x) and y > float(students[i][1]):
            y = float(students[i][1])
    runner = []
    for i in range(len(students)):
        if float(students[i][1]) ==float(y):
            runner.append(students[i][0])
    runner = sorted(runner)
    for i in range(len(runner)):
        print(runner[i])     


# In[ ]:


#FindingthePercentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    output = list(student_marks[query_name])
    per = sum(output)/len(output);
    print("%.2f" % per);


# In[ ]:


#Lists
if __name__ == '__main__':
    N = int(input())
    L=[];
    for i in range(0,N):
        cmd=input().split();
        if cmd[0] == "insert":
            L.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "pop":
            L.pop();
        elif cmd[0] == "print":
            print(L)
        elif cmd[0] == "remove":
            L.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            L.sort();
        else:
            L.reverse();


# In[ ]:


#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))


# In[ ]:


#IntroductionToSets
from __future__ import division

def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':


# In[ ]:


#NoIdea!
if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    
    good = set(map(int, input().strip().split(' ')))
    bad = set(map(int, input().strip().split(' ')))
    
    for i in arr:
        if i in good:
            happiness += 1
        elif i in bad:
            happiness -= 1
    print(happiness)


# In[ ]:


#SymmetricDifference
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Symmetric Difference in Python - Hacker Rank Solution
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Symmetric Difference in Python - Hacker Rank Solution START
M = int(input())
mset = set(map(int, input().split()))
N = int(input())
nset = set(map(int, input().split()))

mdef = mset.difference(nset)
ndef = nset.difference(mset)

output = mdef.union(ndef)

for i in sorted(list(output)):
    print(i)


# In[ ]:


#Set.add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set()
[a.add(input()) for _ in range(int(input()))]
print(len(a))


# In[ ]:


#Set.discard(),.remove()&.pop()
num = int(input())
data = set(map(int, input().split()))
operations = int(input())

for x in range(operations):
  oper = input().split()
  if oper[0] == "remove":
    data.remove(int(oper[1]))
  elif oper[0] == "discard":
    data.discard(int(oper[1]))
  else:
    data.pop()
    
print(sum(data))


# In[ ]:


#Set.union()Operation
n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())

s1 = set(l)
s2 = set(k)

print(len(s1.union(s2)))


# In[ ]:


#Set.intersection()Operation
num1, st1, num2, st2 = (set(input().split()) for i in range(4))
print(len(st1.intersection(st2)))


# In[ ]:


#Set.difference()Operation
n1 = int(input())
set_1 = set(map(int,input().split()))
n2 = int(input())
set_2 = set(map(int,input().split()))
print(len(set_1-set_2))


# In[ ]:


#Set.symmetric_difference()Operation
_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.symmetric_difference(b)))


# In[ ]:


#SetMutations
if __name__ == '__main__':
    (_, A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)

    print (sum(A))


# In[ ]:


#TheCaptain'sRoom
N = int(input())

storage = map(int, input().split())
storage = sorted(storage)

for i in range(len(storage)):
    if(i != len(storage)-1):
        if(storage[i]!=storage[i-1] and storage[i]!=storage[i+1]):
            print(storage[i])
            break;
    else:
        print(storage[i])


# In[ ]:


#CheckSubset
for i in range(int(input())):
    a = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))
    if len(set_a - set_b) == 0:
        print("True")
    else:
        print("False")


# In[ ]:


#CheckStrictSuperset
storage = set(input().split())
N = int(input())
output = True

for i in range(N):
    storage2 = set(input().split())
    if not storage2.issubset(storage):
        output = False
    if len(storage2) >= len(storage):
        output = False

print(output)

