#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

def countGroups(related):
    # Write your code here
    def buildgraph(related):

        graph = {node:[] for node in range(len(related))}

        for i in range(related[0]):
            for j in range(len(related[0])):
                if i!=j and related[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

    graph = buildgraph(related)
    visited = set()
    connected_components = 0
    
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
    
    for node in range(len(graph)//2):
        if node not in visited:
            connected_components += 1
            visited.add(node)
            dfs(node)
    
    return connected_components
    

if __name__ == '__main__':