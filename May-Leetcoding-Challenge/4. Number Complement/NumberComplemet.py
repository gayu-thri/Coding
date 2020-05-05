class Solution:
    def findComplement(self, num: int) -> int:
        # num = 5 -> 101. Desired output is 010 which is 2.
        #left shift 1 to perform XOR with the whole binary number
        # 101       100      110
        #   1 ^      1  ^    1   ^
        # -----     ----     ----
        # 100       110      010
        #CONDITION : perform right shift in a temp variable assigned value as num >> 1 => 101 ; 10 ; 1 ; 0
        #while temp ! = 0 perform xor.
        bit = 1
        temp = num
        while(temp != 0):
            num = num ^ bit
            bit = bit << 1
            temp = temp >> 1
        
        return num
    
        '''
        num = (bin(num))
        res = ''.join(['0' if r == '1' else '1' for r in num[2:]])
        return int(res,2)
        '''   
        '''
        return ~num + 2**(len(bin(num)))
        '''