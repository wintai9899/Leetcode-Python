#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        
        
        # validate startpoint and endpoint
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        # 1d matrix 
        if ROWS == 1:
            return 1
        
        q = [(0,0)]
        step = 1
        while q:
            for _ in range(len(q)):
                row,col = q.pop(0)
                for dr,dc in directions:
                    r = row + dr 
                    c = col + dc 

                    if r == ROWS or r < 0 or c == COLS or c < 0 or grid[r][c]==1 or (r,c) in visited:
                        continue
                    
                    visited.add((r,c))
                    q.append((r,c))

                    if r == ROWS -1 and c == COLS -1:
                        return step + 1
            
            step += 1
        
        return -1
# @lc code=end

