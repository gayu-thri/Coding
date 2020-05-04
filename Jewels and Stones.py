# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:41:38 2020

@author: egayu
"""

J = ['a','b','A']
S = ['a','c','d','A','A','b','b','b']

setj = set(J)
a = sum([stone in setj for stone in S])