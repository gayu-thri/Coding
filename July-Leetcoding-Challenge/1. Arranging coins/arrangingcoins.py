class Solution:
    def arrangeCoins(self, n: int) -> int:
        #binary search
        left = 0, right = n
        while(left <= right):
            k = left + (left-right)//2
            curr = k*(k+1)//2
            if curr == n:
                return k
            elif curr > n:
                right = k-1
            else:
                left = k+1
            
        return right    #Maximum no. of items such that(k*(k+1)//2) <= n 