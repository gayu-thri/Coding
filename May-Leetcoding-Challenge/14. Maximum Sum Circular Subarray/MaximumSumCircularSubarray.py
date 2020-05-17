class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        
        if n == 1:
            return A[0]
        
        if n == 2:
            if A[0] == A[1]:
                return sum(A)
            else:   
                return max(A[0], A[1])
            
        maxTotal,maxcur,mincur,minTotal,s = A[0], A[0], A[0], A[0],A[0]
        for i in range(1, len(A)):
            maxcur = max(A[i], maxcur + A[i])
            maxTotal = max(maxTotal, maxcur)            
            
            mincur = min(A[i], mincur + A[i])            
            minTotal = min(minTotal, mincur)            
            s += A[i]
            
        if(s == mincur):
            return maxTotal
        
        return max(s - minTotal, maxTotal);
    
    
'''
EXPLANATION:-
EX 1:-
   A = [1, -2, 3, -2]
   max = 3   (This means max subarray sum for normal array)
   min = -2  (This means min subarray sum for normal array)
   sum = 0   (total array sum)
   Maximum Sum = 3 (max)

EX2:-
  A = [5, -3, 5]
  max = 7
  min  = -3
  sum = 7
  maximum subarray sum = 7 - (-3) = 10
  
EX3:-
   A = [3, -1, 2, -1]
   max = 4
   min = -1
   sum = 3
   maximum subarray sum  = sum - min = 3 - (-1) = 4

EX4:-
   A = [-2, -3, -1]
   max = -1
   min = -6
   sum = -6
   In this example, if we do (sum - min) then result is 0. but there is no subarray with sum 0.
   So, in this case we return max value. that is -1.
'''