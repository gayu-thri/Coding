class Solution {
    public int findJudge(int N, int[][] trust) 
    {
        int[] indegree = new int[N];
        int[] outdegree = new int[N];
        
        Arrays.fill(indegree,0,N, 0);
        Arrays.fill(outdegree,0,N, 0);
        
        for(int i=0; i<trust.length ; i++)
        {
            int a = trust[i][0] - 1;
            int b = trust[i][1] - 1;
            
            indegree[b] += 1;
            outdegree[a] += 1;
        }
        
        for(int x=0 ; x<N ; x++)
        {
            if(outdegree[x] == 0 && indegree[x] == N-1)
                return x+1;
        }
        return -1;
    }
}