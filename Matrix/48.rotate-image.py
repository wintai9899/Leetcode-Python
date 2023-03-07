#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0 
        right = len(matrix) - 1
        
        while left < right:
            for i in range(right - left):
                # pointers
                top = left
                bot = right
                
                # save topleft value into temp variable
                topleft = matrix[top][left + i]
                
                # map first col to first row 
                matrix[top][left + i] = matrix[bot - i][left]
                
                # map last row to first col 
                matrix[bot - i][left] = matrix[bot][right - i]
                
                # map last col to last row 
                matrix[bot][right - i] = matrix[top + i][right]
                
                # map first row to last col 
                matrix[top + i][right] = topleft
            
            left += 1
            right -= 1
        
        
        
# @lc code=end

