#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (44.38%)
# Likes:    5147
# Dislikes: 198
# Total Accepted:    285.5K
# Total Submissions: 642.2K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given two strings s and t, return the number of distinct subsequences of s
# which equals t.
# 
# The test cases are generated so that the answer fits on a 32-bit signed
# integer.
# 
# 
# Example 1:
# 
# 
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# 
# 
# Example 2:
# 
# 
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.
# 
# 
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = 0
        # find the number of distinct subsequences
        #      i              j
        # s = "rabbbit", t = "rabbit"

        cache = {}  # (i,j): number of ways
        def dfs(i,j):
            # base case: finished t -> found 1 distinct solution
            if j == len(t):
                return 1
            # finished s but not done with t -> no solution found
            if i == len(s):
                return 0
            
            # check if in cache
            if (i,j) in cache:
                return cache[(i,j)]

            # move on if s[i] == t[j]
            # option: move both pointers or juz move i
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            # search with other chars in s
            else:
                cache[(i,j)] = dfs(i+1,j)
            
            return cache[(i,j)]

        res = dfs(0,0)

        return res

        
# @lc code=end

