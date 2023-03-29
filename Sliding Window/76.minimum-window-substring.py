#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (40.86%)
# Likes:    14626
# Dislikes: 621
# Total Accepted:    986K
# Total Submissions: 2.4M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
# 
# The testcases will be generated such that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
# 
# 
# Example 2:
# 
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# 
# Example 3:
# 
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# 
# 
# Constraints:
# 
# 
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        sCount = {}
        
        have = 0
        needed = len(tCount)
        
        minWindow = float("inf")
        res = [-1,-1]
        
        l = 0
        
        for r in range(len(s)):
            sCount[s[r]] = sCount.get(s[r],0) + 1
            
            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1
                
            while have == needed:
                # compute window
                curWindow = r - l + 1
                if curWindow < minWindow:
                    minWindow = min(curWindow, minWindow)
                    res = [l,r]
                
                # shift window
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]: 
                    have -= 1
                l += 1
                
        l,r = res
        return s[l:r+1] if minWindow != float('inf') else ""
        
# @lc code=end

