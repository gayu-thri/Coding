# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 00:14:17 2020

@author: egayu
"""
from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)
        
    def addedge(self, u, v):
        self.graph[u].append(v)
        
    def helper(self, v, visited, stack):
        
        visited[v] = True
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.helper(i, visited, stack)
                
        stack.append(v)
        
    def topological_sort(self):
        
        visited = [False] * self.v
        stack = []
        
        for i in range(self.v):
            if visited[i] == False:
                self.helper(i, visited, stack)
        
        print(stack[::-1])
        
g = Graph(6)
g.addedge(5, 2) 
g.addedge(5, 0) 
g.addedge(4, 0) 
g.addedge(4, 1)     
g.addedge(2, 3) 
g.addedge(3, 1) 

g.topological_sort()
  