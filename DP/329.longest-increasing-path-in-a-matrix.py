#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (52.42%)
# Likes:    7836
# Dislikes: 116
# Total Accepted:    437.9K
# Total Submissions: 835.1K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an m x n integers matrix, return the length of the longest increasing
# path in matrix.
# 
# From each cell, you can either move in four directions: left, right, up, or
# down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        dp = {} # (r,c) : longest incresing path length 

        def dfs(r,c,prevNum):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevNum:
                return 0

            # return if in cache
            if (r,c) in dp:
                return dp[(r,c)]

            res = 1
            res = max(res, dfs(r-1,c,matrix[r][c]) + 1)
            res = max(res, dfs(r+1,c,matrix[r][c]) + 1)
            res = max(res, dfs(r,c-1,matrix[r][c]) + 1)
            res = max(res, dfs(r,c+1,matrix[r][c]) + 1)

            dp[(r,c)] = res

            return res
            

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)

        lip = max(dp.values())

        return lip

        
# @lc code=end

