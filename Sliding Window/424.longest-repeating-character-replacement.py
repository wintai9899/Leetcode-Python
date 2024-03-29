#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (51.85%)
# Likes:    7662
# Dislikes: 319
# Total Accepted:    427K
# Total Submissions: 822.5K
# Testcase Example:  '"ABAB"\n2'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
# 
# 
# Example 1:
# 
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# 
# Example 2:
# 
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# 
# 
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        res = 0
        l = 0
        # keeps track of the majority elements in the sliding window
        majority = 0
        
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r],0) + 1
            majority = max(majority, hashmap[s[r]])
            # replacement needed = windowSize - majority elements 
            # condition must hold: replacement_needed must <= k 
            
            # shift the window when replacement_needed > k
            while (r - l + 1) - majority > k:
                hashmap[s[l]] -= 1
                l +=  1
            
            res = max(res, r-l+1)
        return res
        
# @lc code=end

