# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:10:03 2020

@author: egayu
"""

def findmin(s):
    strRev = s[::-1]
    n = len(s)
    m = len(strRev)
    dp = [[0]*(m+1) for i in range(n+1)]
    print(dp)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == strRev[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    return len(s) - dp[n][m]

s = "abcbd"
n = findmin(s)
print(n)
