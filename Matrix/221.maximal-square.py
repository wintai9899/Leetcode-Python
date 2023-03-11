#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        cache = {}
        
        def helper(r,c):
            if r == ROWS or c == COLS:
                return 0 
            
            if (r,c) not in cache:
                down = helper(r+1,c)
                left = helper(r,c+1)
                diag = helper(r+1,c+1)
                
                cache[(r,c)] = 0
            
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down, left, diag)
            return cache[(r,c)]

        helper(0,0)
        maxLength = max(cache.values())
        res = maxLength ** 2
        return res
# @lc code=end

