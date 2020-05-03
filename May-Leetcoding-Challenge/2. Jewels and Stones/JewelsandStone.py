class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # create a dict for reducing run time
        stones = dict()
        for stone in S:
            if stone in stones:
                stones[stone] += 1
            else:
                stones[stone] = 1
        myjewels = 0
        for jewel in J:
            if jewel in stones:
                myjewels += stones[jewel]
        
        return myjewels

        '''
        #set contains unique elements. 
        #jewels need not not have duplicate elements
        setj = set(J)
        return sum(stone in setj for stone in S)
        '''
        '''
        jewels = set(J)
        count = 0
        for stone in S:
            if stone in jewels:
                count += 1
                
        return count
        '''