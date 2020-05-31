class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
         
        a = len(word1)
        b = len(word2)
        
        dp = [[0 for i in range(a+1)] for j in range(b+1)]
        '''
        for k in range(a):
            dp[0][k] = k
        for k in range(b):
            dp[k][0] = k
        '''
        for i in range(b+1):
            for j in range(a+1):
                
                if i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                
                #i and j >= 1, I should also check index 0
                elif word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        print(dp)
        return dp[b][a] 