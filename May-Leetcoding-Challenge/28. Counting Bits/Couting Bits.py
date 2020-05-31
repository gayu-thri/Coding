class Solution:
    def countBits(self, num: int) -> List[int]:
        
        if num == 0:
            return [0]
        dp = [0,1]
        if num == 1:
            return dp
        
        for i in range(2,num+1):
            if(i%2):
                #if i is odd
                dp.append(dp[i//2] + dp[i%2])
            else:
                #if i is even
                dp.append(dp[i//2])
                
        return dp