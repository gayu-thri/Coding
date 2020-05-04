# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:17:41 2020

@author: egayu
"""
class Solution: 
    def exist(self, board, word): 
        """ :type board: List[List[str]] 
            :type word:str 
            :rtype: bool 
            """ 
        def dfs(i, j, word, x): 
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j]!= word[x]: 
                return 
            
            if x == len(word) - 1: 
                return True 
            
            copy = board[i][j] 
            board[i][j] = '#'   #As it is already visited, We change it to '#' 
            
            #[0,0] --> down=[1,0] ; up=[-1,0] ; right=[0,1] ; left=[0,-1] 
            up = dfs(i-1, j, word, x+1) 
            if up == True: 
                return True 
            
            down = dfs(i+1, j, word, x+1) 
            if down == True: 
                return True
            
            left = dfs(i, j-1, word, x+1) 
            if left == True: 
                return True 
            
            right = dfs(i, j+1, word, x+1) 
            if right == True: 
                return True  
            
            
            
            board[i][j] = copy      #if not matching with any adjacent # is not replaced 
        
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if word[0] == board[i][j]:
                    x = 0 
                    res = dfs(i, j, word, x) 
                    if res == True: 
                        return True 
        return False
