class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #In a sorted array => Binary Search
        left = 0
        right = len(nums) - 1
        
        while(left < right):
            mid = left + (right - left)//2
            isrighteven = (right - mid)%2 == 0 #check right half's length
            
            if nums[mid] == nums[mid-1]:
                if isrighteven == True:
                    right = mid - 2     #skip the dup mid element
                else:
                    left = mid + 1
            
            elif nums[mid] == nums[mid+1]:
                if isrighteven == True:
                    left = mid + 2
                else:
                    right = mid - 1
            
            else:
                return nums[mid]
        
        return nums[left]