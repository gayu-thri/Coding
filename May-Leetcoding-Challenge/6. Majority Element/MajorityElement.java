class Solution {
    public int majorityElement(int[] nums) 
    {
        if(nums.length == 1){
            return nums[0];
        }
        
        HashMap<Integer, Integer> freq = new HashMap<Integer, Integer>();
        for(int i:nums){
            if(freq.containsKey(i) && freq.get(i) + 1 > nums.length/2)
                return i;
            else
                freq.put(i, freq.getOrDefault(i,0) + 1); 
                         /*f it's never we will make it occur once, if it exists get(i) + 1 */
        }
        return -1;
    }
}