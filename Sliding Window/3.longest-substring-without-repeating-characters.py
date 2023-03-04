#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() 
        l = 0
        res = 0 
        for r in range(len(s)):
            
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1 
            else:
                charSet.add(s[r])
            
            windowSize = r - l + 1 
            res = max(res, windowSize)
            
            
        return res

# @lc code=end

