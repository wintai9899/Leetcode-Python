#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        
        def dfs(r,c,i):
            # word found
            if i == len(word):
                return True
            
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in path or board[r][c] != word[i]:
                return

            path.add((r,c))
            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        
        return False
        
# @lc code=end

