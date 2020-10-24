# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#wordsplit-norton

string = input("Enter the string: \n")

substrings = []
k = 0
substrings.append(string[0])
for i in range(1, len(string)):
    if string[i] not in substrings[k]:
        substrings[k] += string[i]
    else:
        k += 1
        substrings.insert(k, string[i])

print("\nCount of word split: ",len(substrings))
print("Substrings: ", substrings)