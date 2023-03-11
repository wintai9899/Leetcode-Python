#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]
        
        for r in range(1,m):
            for c in range(1,n):
                # cur path sum = top sum + left sum
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]
                
# Brute force solution using Recursion 

# def uniquePaths(self, m: int, n: int) -> int:
        
#         dp = {(m-1,n-1): 1}

#         def dfs(r,c):
#             if r < 0 or r== m or c < 0 or c == n:
#                 return 0
            
#             if (r,c) in dp:
#                 return dp[(r,c)]
            
#             dp[(r,c)] = dfs(r+1,c) + dfs(r,c+1)

#             return dp[(r,c)]
        
#         return dfs(0,0)
# @lc code=end

