#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (51.07%)
# Likes:    10933
# Dislikes: 607
# Total Accepted:    954.4K
# Total Submissions: 1.9M
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row
# and column to 0's.
# 
# You must do it in place.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
# 
# 
# 
# Follow up:
# 
# 
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowToZero = []
        colToZero = []

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowToZero.append(r)
                    colToZero.append(c)

        for r in range(ROWS):
            for c in range(COLS):
                if r in rowToZero or c in colToZero:
                    matrix[r][c] = 0
        
# @lc code=end

