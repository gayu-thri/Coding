class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        dp = []
        
        for i in nums:
            sum = max(sum + i, i)
            dp.append(sum)

        return max(dp)
        
            