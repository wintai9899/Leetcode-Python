#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxWindowSize = 0
        # try every pair and expand outwards
        for i in range(len(s)):
            # handle even length 
            l,r = i,i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tempWindow = r - l + 1
                if tempWindow > maxWindowSize:
                    maxWindowSize = tempWindow
                    res = s[l:r+1]
                # expand outwards
                l -= 1
                r += 1
            
            l,r = i, i + 1
            # handle odd length 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tempWindow = r - l + 1
                if tempWindow > maxWindowSize:
                    maxWindowSize = tempWindow
                    res = s[l:r+1]
                # expand outwards
                l -= 1
                r += 1
        
        return res
                        
        
        
# @lc code=end

