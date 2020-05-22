class Solution {
    public int maxSubarraySumCircular(int[] A) {
        int n = A.length;
        
        if(n == 1)
            return A[0];
        
        if(n == 2)
        {
            if(A[0] == A[1])
                return A[0] + A[1];
            else 
                return Math.max(A[0], A[1]);
        }  
        int maxTotal = A[0], maxcur = A[0], mincur = A[0], minTotal = A[0], s = A[0];
        for(int i = 1; i<A.length; i++)
        {
            maxcur = Math.max(A[i], maxcur + A[i]);
            maxTotal = Math.max(maxTotal, maxcur);       
            
            mincur = Math.min(A[i], mincur + A[i]);            
            minTotal = Math.min(minTotal, mincur);           
            s += A[i];
        }  
        if(s == mincur)
            return maxTotal;
        
        return Math.max(s - minTotal, maxTotal);
    }
}