class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        lena = len(A)
        lenb = len(B)
        
        dp = [[0 for i in range(lenb+1)] for j in range(lena+1)]
        
        for i in range(lena):
            for j in range(lenb):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                
        return dp[lena][lenb]