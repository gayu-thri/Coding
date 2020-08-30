# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:00:56 2020

@author: egayu
"""

n = int(input())
arr = []
i, step = 1, 1
while(i<n+1):
    for j in range(step):
        print(i, end=" ")
        i += 1
    step += 1
    print("\n")

print("Steps", step-1)
temp = n
last_step_elements = []
for i in range(step-1):
    last_step_elements.append(temp)
    temp = temp - 1

last_step_elements.reverse()
print(last_step_elements)
