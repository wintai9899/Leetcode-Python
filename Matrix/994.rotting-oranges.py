#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = [] 
        freshOranges = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshOranges += 1
                
                elif grid[r][c] == 2:
                    q.append((r,c))
        time = 0
        while q and freshOranges > 0:
            for _ in range(len(q)):
                row,col = q.pop(0)
                
                for dr, dc in directions:
                    r = row + dr 
                    c = col + dc
                    
                    if r == ROWS or r < 0 or c == COLS or c < 0 or grid[r][c] != 1:
                        continue       
                    
                    q.append((r,c))
                    grid[r][c] = 2
                    freshOranges -= 1
                    
            time += 1 
        
        return time if freshOranges == 0 else -1
            
# @lc code=end

