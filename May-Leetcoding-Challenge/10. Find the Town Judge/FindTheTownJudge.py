class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        #  N people labelled from 1 to N
        # GRAPH THEORY
        indegree = [0] * N
        outdegree = [0] * N
        
        for a, b in trust:      #no. of vertices - V
            a -= 1
            b -= 1  #index starts from 0 
            
            outdegree[a] += 1
            indegree[b] += 1
            
        for x in range(N):  #no. of edges - E
            if outdegree[x] == 0 and indegree[x] == N-1:
                return x+1
        ''' total run time - O(V+E) '''
        return -1
            