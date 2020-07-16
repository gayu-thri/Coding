# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:43:59 2020

@author: egayu
"""

import string

def countwords(sentence):
    count = 0
    
    l = sentence.split()
    
    for ch in l:
        if ch.strip(string.punctuation).isalpha() or ch.isalpha() or ch.find('-') != -1:
            count += 1
    return count

sentence = input()
result = countwords(sentence)
print(str(result))
