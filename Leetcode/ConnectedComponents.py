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

	def print(self):
		print('Adjacency list: ', self.adj)

	def connected_component(self):
		visited = set()
	    connected = 0
	    def dfs(node):
	        for neighbor in adj[node]:
	            if neighbor not in visited:
	                visited.add(neighbor)
	                dfs(neighbor)
	    
	    for node in range(len(adj)//2):
	        if node not in visited:
	            connected += 1
	            visited.add(node)
	            dfs(node)
	    
	    return connected


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