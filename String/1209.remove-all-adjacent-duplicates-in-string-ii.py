#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
#
# algorithms
# Medium (56.17%)
# Likes:    5006
# Dislikes: 94
# Total Accepted:    260.4K
# Total Submissions: 463.6K
# Testcase Example:  '"abcd"\n2'
#
# You are given a string s and an integer k, a k duplicate removal consists of
# choosing k adjacent and equal letters from s and removing them, causing the
# left and the right side of the deleted substring to concatenate together.
# 
# We repeatedly make k duplicate removals on s until we no longer can.
# 
# Return the final string after all such duplicate removals have been made. It
# is guaranteed that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# 
# Example 2:
# 
# 
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# 
# Example 3:
# 
# 
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 2 <= k <= 10^4
# s only contains lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (char, count)
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1

            else:
                stack.append([char,1])
                
            if stack[-1][1] == k:
                stack.pop()
        
        res = ""
        
        for char,count in stack:
            curStr = str(count * char)
            res += curStr
        
        return res
        
# @lc code=end

