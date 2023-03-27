#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (34.07%)
# Likes:    4302
# Dislikes: 106
# Total Accepted:    202.5K
# Total Submissions: 594.1K
# Testcase Example:  '"()"'
#
# Given a string s containing only three types of characters: '(', ')' and '*',
# return true if s is valid.
# 
# The following rules define a valid string:
# 
# 
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis
# ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string "".
# 
# 
# 
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "(*)"
# Output: true
# Example 3:
# Input: s = "(*))"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.
# 
# 
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax, leftMin = 0,0

        for c in s:
            if c == "(":
                leftMax += 1
                leftMin += 1
            
            elif c == ")":
                leftMax -= 1
                leftMin -= 1
            
            else:
                # * 
                leftMax += 1
                leftMin -= 1
            
            if leftMax < 0:
                return False
            
            if leftMin < 0:
                leftMin = 0
            
        return leftMin == 0
        
# @lc code=end

