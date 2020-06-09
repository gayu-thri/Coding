class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n == 1):
            return True
        if(n == 0):
            return False
        
        while n % 2 == 0:
            n = n//2
            
        if(n == 1):
            return True
        else:
            return False