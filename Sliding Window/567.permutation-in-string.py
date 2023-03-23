#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.36%)
# Likes:    9521
# Dislikes: 303
# Total Accepted:    626.8K
# Total Submissions: 1.4M
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 in s2
        l = 0
        r = 0
        s1Count = self.getCount(s1)

        for r in range(len(s1)-1, len(s2)):
            getCharCount = self.getCount(s2[l:r+1])
            if getCharCount == s1Count:
                return True
            
            l += 1
        
        return False
    
    def getCount(self, curArr):
        hashmap = {}

        for char in curArr:
            hashmap[char] = hashmap.get(char,0) + 1
        
        return hashmap
        
# @lc code=end

