#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (64.74%)
# Likes:    10422
# Dislikes: 327
# Total Accepted:    628K
# Total Submissions: 969.2K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
# 
# 
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 16
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []
        
        def backtrack(i):
            if i == len(s):
                res.append(part.copy())
                return
            # i = left, j = right pointer
            for j in range(i, len(s)):
                if self.isPalindrome(i,j,s):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()                    
    
        backtrack(0)
        
        return res

    def isPalindrome(self, l,r,s):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
        return True
        
# @lc code=end

