class Solution {
    public int singleNonDuplicate(int[] nums) 
    {
        int left = 0;
        int right = nums.length-1;
        
        while(left < right)
        {
            int mid = left + (right-left)/2;
            boolean isrighteven = (right-mid) % 2 == 0;
            
            if(nums[mid] == nums[mid-1])
            {
                if(isrighteven == true)
                    right = mid - 2;
                else
                    left = mid + 1;
            }
            else if(nums[mid] == nums[mid+1])
            {
                if(isrighteven == true)   //3 3 4 4 8 8 if it's odd then move the right pointer.
                    left = mid + 2;
                else
                    right = mid - 1;
            }
            else
                return nums[mid];
        }
        return nums[left];        
    }
}