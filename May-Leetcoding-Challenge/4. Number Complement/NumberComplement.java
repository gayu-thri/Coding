class Solution {
    public int findComplement(int num)
    {
        //num = 5 -> 101. Desired output is 010 which is 2.
        //left shift 1 to perform XOR with the whole binary number
        //101       100      110
        //  1 ^      1  ^    1   ^
        //-----     ----     ----
        //100       110      010
        //CONDITION : perform right shift in a temp variable assigned value as num >> 1 => 101 ; 10 ; 1 ; 0
        //while temp ! = 0 perform xor.
        
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
