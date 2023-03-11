#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # eg. newS = s + s = "abcde" + "abcde" = "abcdeabcde"
        # this newS constains every possible shifts for s
        # so just look for goal in s return True if exists
        # "ab  cdeab  cde"
        # it does exist in the string 
        if len(s) != len(goal): return False
        newStr = s + s
        return goal in newStr
        
# @lc code=end

