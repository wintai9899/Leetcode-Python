#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 1 and s.isdigit():
            return ""
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                # build substring 
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr
                
                # remove "["
                stack.pop()
                
                # handle multiplier
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                    # build output string
                # put back on stack
                stack.append(int(k) * subStr)
        return "".join(stack)
        
# @lc code=end

