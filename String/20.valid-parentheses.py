#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ")" : "(", 
            "}" : "{",
            "]" : "["
        }
        
        stack = []
        
        for char in s:
            if char in hashmap:
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                
                else:
                    # wrong order, not possible
                    return False
            else:
                stack.append(char)

        return True if not stack else False
            
            
        
# @lc code=end

