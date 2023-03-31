#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Easy (75.70%)
# Likes:    8602
# Dislikes: 411
# Total Accepted:    751K
# Total Submissions: 991.6K
# Testcase Example:  '2'
#
# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of
# i.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 
# 
# Example 2:
# 
# 
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^5
# 
# 
# 
# Follow up:
# 
# 
# It is very easy to come up with a solution with a runtime of O(n log n). Can
# you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
# 
# 
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        count 1s
        n
        # offset = 1
        0 : 000000 00 -> 0
        1 : 000000 01 -> 1

        # offset = 2 
        2 : 000000 10 -> 1 (1 + dp[n-2] = 1 + dp[0] = 1)
        3 : 000000 11 -> 2 (1 + dp[n-2] = 1 + dp[1] = 2)

        # offset = 4 = most significant bit
        4 : 000001 00 -> 1  (1 + dp[n-4] = 1 + dp[4-4] = 1 + 0 = 1)
        5 : 000001 01 -> 2  (1 + dp[n-4] = 1 + dp[5-4] = 1 + dp[1] = 2)
        6 : 000001 10 -> 2  (1 + dp[n-4] = 1 + dp[6-4] = 1 + dp[2] = 2)
        7 : 000001 11 -> 3  (1 + dp[n-4] = 1 + dp[7-4] = 1 + dp[3] = 3)
        
        # offset doubles (offset = MSB = 8)
        8 : 000010 00 -> 1  (1 + dp[n-8] = 1 + dp[8-8] = 1 + dp[0] = 1)
        """

        dp = [0] * (n+1)
        offset = 1 

        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i 
            
            dp[i] = 1 + dp[i-offset]
        
        return dp

    
        
# @lc code=end

