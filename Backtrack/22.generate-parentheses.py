#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (72.44%)
# Likes:    17233
# Dislikes: 696
# Total Accepted:    1.4M
# Total Submissions: 1.9M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openCount, closeCount):
            # base case
            if openCount == closeCount == n:
                output = "".join(stack.copy())
                res.append(output)
                return 

            # need more openCOunt
            if openCount < n:
                stack.append("(")
                backtrack(openCount+1, closeCount)
                stack.pop()
            
            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()

        backtrack(0,0)
        return res
        
# @lc code=end

