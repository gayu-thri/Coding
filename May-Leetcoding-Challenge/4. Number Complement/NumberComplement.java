class Solution {
    public int findComplement(int num)
    {
        int res = 0;
        int bit = 1;
        while(num > 0)
        {
            res = res + (num % 2 ^ 1) * bit;
            bit = bit << 1;
            num = num >> 1;
        }
        return res;
    }
}