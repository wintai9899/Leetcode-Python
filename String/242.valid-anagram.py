#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = {}
        tCount = {} 

        for i in range(len(s)):
            sCount[s[i]]  = sCount.get(s[i],0) + 1
            tCount[t[i]] = tCount.get(t[i],0) + 1

        return sCount == tCount
        
# @lc code=end

