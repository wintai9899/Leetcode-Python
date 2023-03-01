#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0 
        visited = set() 
        
        def dfs(r,c):
            if r == ROWS or r < 0 or c == COLS or c < 0 or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1) + 1
        
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r,c))
                
        return maxArea
        
# @lc code=end

