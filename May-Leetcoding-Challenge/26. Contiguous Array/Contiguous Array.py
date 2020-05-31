class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, subarr = 0, 0
        mydict = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count == 0:
                subarr = i + 1
            if count in mydict:
                subarr = max(subarr, i - mydict[count])
            else:
                mydict[count] = i
        
        return subarr