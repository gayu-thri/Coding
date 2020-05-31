class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = collections.defaultdict(set)
        outdegree = collections.defaultdict(set)
        
        for x,y in prerequisites:
            indegree[x].add(y)
            outdegree[y].add(x)
            
        connection_removed = 0
        indegree_zero = list()
        
        for i in range(numCourses):
            if not indegree[i]:
                indegree_zero.append(i)
                connection_removed += 1
        while indegree_zero:
            curr_node = indegree_zero.pop()
            for neighbor in outdegree[curr_node]:
                indegree[neighbor].remove(curr_node)
                if not indegree[neighbor]:
                    indegree_zero.append(neighbor)
                    connection_removed += 1 
        
        return (connection_removed == numCourses)   #reduced == nodes for true