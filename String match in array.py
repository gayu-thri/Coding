# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:52:12 2020

@author: egayu
"""

class Solution:
    def stringMatching(self, words):
        #need to sort words using length in ascending order
        words = sorted(words,key = len) #sorts using length as the key
        #words.reverse()
        print('Sorted words: ',words)
        substrings = []
        
        for i in range(len(words)):
            
            for j in range(i+1, len(words)):
                
                if words[i] in words[j]:
                    #Once substring matches break from inner for loop
                    substrings.append(words[i])
                    break
        return substrings

s = Solution()
print('Enter the words of the superset Ex: mass as hero superhero')
words = list(map(str,input().split()))
match = s.stringMatching(words)
print('Substring match: ',match)
