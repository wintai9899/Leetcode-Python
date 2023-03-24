#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (54.39%)
# Likes:    6221
# Dislikes: 1190
# Total Accepted:    348.1K
# Total Submissions: 639.8K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
# 
# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea
# level of the cell at coordinate (r, c).
# 
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height
# is less than or equal to the current cell's height. Water can flow from any
# cell adjacent to an ocean into the ocean.
# 
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
# 
# 
# Example 1:
# 
# 
# Input: heights =
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans,
# as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
# [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
# [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
# [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
# [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
# [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
# [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
# ⁠      [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the
# Pacific and Atlantic oceans.
# 
# 
# Example 2:
# 
# 
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and
# Atlantic oceans.
# 
# 
# 
# Constraints:
# 
# 
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start dfs in the reverse order
        # start at the border, and keep dfs into the center of the island. 
        # condition: height should be increasing from the border to the center. 

        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set() 
        res = []

        def dfs(r,c, visited, prevHeight):
            if r == ROWS or r < 0 or c == COLS or c < 0 or heights[r][c] < prevHeight or (r,c) in visited:
                return 
            
            visited.add((r,c))
            
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
    
        # Iterate first row (pacific) and last row (atlantic)
        for c in range(COLS):
            # pacific
            dfs(0, c, pacific, heights[0][c])

            # atlantic
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        # Iterate first col (pacific) and last col (atlantic)
        for r in range(ROWS):
            dfs(r,0,pacific, heights[r][0])
            dfs(r,COLS-1, atlantic, heights[r][COLS-1])

        for r in range(ROWS):
            for c in range(COLS):
                # able to flow to both oceans
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        
        return res




    

        
# @lc code=end

