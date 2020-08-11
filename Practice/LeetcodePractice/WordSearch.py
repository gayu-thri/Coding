class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, word, count):
            
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or word[count] != board[i][j]:
                return 
            
            if count == len(word) - 1:
                return True
            
            copy = board[i][j]
            board[i][j] = '#'
            
            up = dfs(i-1, j, word, count+1)
            if up == True:
                return True
            
            right = dfs(i, j+1, word, count+1)
            if right == True:
                return True
            
            down = dfs(i+1, j, word, count+1)
            if down == True:
                return True
            
            left = dfs(i, j-1, word, count+1)
            if left == True:
                return True
            
            board[i][j] = copy
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    count = 0
                    ret = dfs(i, j, word, count)
                    if ret == True:
                        return True
        return False
    