#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()
        
        def dfs(r,c):
            if r == ROWS or r < 0 or c == COLS or c < 0 or grid[r][c] == "0" or (r,c) in visited:
                return 0 
            visited.add((r,c))
            
            return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1) + 1
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1 
        
        return islands 
        
        
            
        
        
# @lc code=end
