#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (66.82%)
# Likes:    8791
# Dislikes: 188
# Total Accepted:    558.1K
# Total Submissions: 835K
# Testcase Example:  '"abc"'
#
# Given a string s, return the number of palindromic substrings in it.
# 
# A string is a palindrome when it reads the same backward as forward.
# 
# A substring is a contiguous sequence of characters within the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# Example 2:
# 
# 
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0

        for i in range(len(s)):
            
            res += self.countLength(s,i,i)
            res += self.countLength(s,i,i+1)
            
            
        return res

    def countLength(self, s,l,r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        
        return res
        
        
        
# @lc code=end

