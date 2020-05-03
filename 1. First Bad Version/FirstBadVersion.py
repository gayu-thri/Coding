# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Versions: [1,2,3,...,n]
        #if 4 is bad, then [1,2,3,4,5] -> isBadversion() [false,false,false,true,true] [0,0,0,1,1]
        left = 1
        right = n
        #Since sorted, binary search
        while left <= right:
            mid = left + (right - left)//2
            if isBadVersion(mid) == False:      #still a good version, proceed towards right
                left = mid + 1      
            else:     #A bad version encountered, go towards left
                right = mid - 1
        return left
