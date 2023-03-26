#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (45.56%)
# Likes:    13654
# Dislikes: 577
# Total Accepted:    1.3M
# Total Submissions: 2.9M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #Initialize dp array
        dp = [False] * (len(s) + 1)
        
        dp[len(s)] = True
        
        # reverse traverse
        for i in range(len(s) -1, -1, -1):
            for word in wordDict:
                # check if match and in range
                if (i + len(word) <= len(s) and s[i:i+len(word)] == word):
                    dp[i] = dp[i + len(word)]
                
                # if true, skip to next i interation
                if dp[i]:
                    break 
            
        return dp[0]
        
# @lc code=end

