#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Medium (27.41%)
# Likes:    10185
# Dislikes: 11874
# Total Accepted:    2.5M
# Total Submissions: 9.2M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
# 
# 
# Example 1:
# 
# 
# Input: x = 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: x = -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: x = 120
# Output: 21
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648    # -2^31
        MAX = 2147483647     #2^31 - 1
        
        res = 0 
        
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)
            
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX & 10)):
                return 0
            
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            
            # 3 + 2 = 32 -> 3 * 10 + 2
            res = (res * 10) + digit 
            
            
        return res
        
# @lc code=end

