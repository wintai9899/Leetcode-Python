#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        top, left = 0,0
        bot = len(matrix)
        right = len(matrix[0])
        
        while top < bot and left < right:
            # first row 
            for i in range(left, right):
                res.append(matrix[top][i])
            
            top += 1
            
            # last col
            for i in range(top, bot):
                res.append(matrix[i][right-1])
            
            right -= 1
            
            if (top >= bot or right <= left):
                break 
            
            # last row 
            for i in range(right - 1, left- 1, -1):
                res.append(matrix[bot-1][i])
            
            bot -= 1
            
            # first col 
            for i in range(bot-1,top-1,-1):
                res.append(matrix[i][left])
            
            left += 1
        
        return res
                
            
            
                
            
        
# @lc code=end

