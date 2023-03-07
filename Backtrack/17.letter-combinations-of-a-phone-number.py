#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetter = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
         
        res = [] 
         
        def backtrack(i, curStr):
            if i == len(digits):
                res.append(curStr)
                return
             
            for char in digitToLetter[digits[i]]:
                backtrack(i+1, curStr + char)
        
        if digits:
            backtrack(0, "")
        
        return res

# @lc code=end

