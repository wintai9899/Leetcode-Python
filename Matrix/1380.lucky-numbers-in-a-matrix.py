#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # use to store min values of each row
        rowMin = set()
        res = []
        
        for r in range(ROWS):
            rowMin.add(min(matrix[r]))
        
        # look for max in each col
        for c in range(COLS):
            curMax = 0
            for r in range(ROWS):
                if matrix[r][c] > curMax:
                    curMax = matrix[r][c]
            
            if curMax in rowMin:
                res.append(curMax)
        return res
# @lc code=end

