#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (64.46%)
# Likes:    2752
# Dislikes: 336
# Total Accepted:    149.6K
# Total Submissions: 232K
# Testcase Example:  '2'
#
# Suppose you have n integers labeled 1 through n. A permutation of those n
# integers perm (1-indexed) is considered a beautiful arrangement if for every
# i (1 <= i <= n), either of the following is true:
# 
# 
# perm[i] is divisible by i.
# i is divisible by perm[i].
# 
# 
# Given an integer n, return the number of the beautiful arrangements that you
# can construct.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
# ⁠   - perm[1] = 1 is divisible by i = 1
# ⁠   - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
# ⁠   - perm[1] = 2 is divisible by i = 1
# ⁠   - i = 2 is divisible by perm[2] = 1
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 15
# 
# 
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0 
        visited = set() 
        
        def backtrack(cur):
            nonlocal res
            # base case
            if cur > n:
                res += 1
                return 
            
            for i in range(1, n+1):
                if i in visited:
                    continue 
                
                if i % cur == 0 or cur % i == 0:
                    visited.add(i)
                    backtrack(cur+1)
                    visited.remove(i)
        
        
        backtrack(1)
        return res
        
# @lc code=end
