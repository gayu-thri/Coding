# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:49:17 2020

@author: egayu
"""

'''
 Find the connected components & number of components in an UNDIRECTED GRAPH
'''

class Graph:

	def __init__(self, V):

		self.V = V
		self.adj = [[] for i in range(V)]

	def addEdge(self, a, b):
		self.adj[a].append(b)
		self.adj[b].append(a)


	def connected_component(self):
		visited = set()
        connectedComponents = 0
        
        def dfs(node: int):
            if node not in visited:
                visited.add(node)
                
                for nextNode in graph[node]:
                    dfs(nextNode)
            
        for node in range(n):
            if node not in visited:
                connectedComponents += 1
                dfs(node)
            
        return connectedComponents
    
    def print(self):
		print('Adjacency list: ', self.adj)
   


if __name__ == '__main__':

	#graph(n) -> 0 to n-1 vertices - graph class
	g = Graph(7)
	g.addEdge(0, 1)
	g.addEdge(1, 2)
	g.addEdge(3, 4)
	g.addEdge(5, 6)

	g.print()	#adjacency list

	components = g.connected_component()
	print(components)
