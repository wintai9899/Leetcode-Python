#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        # edge case 
        if n == 1:
            return "1"

        def sayNumber(n):
            # convert to string
            s = str(n)
            # left pointer
            left = s[0]
            count = 1 
            output = ""

            for right in s[1:]:
                if right == left:
                    count += 1
                
                else:
                    # build string
                    output += str(count) + left
                    # move left pointer
                    left = right 
                    # reset count 
                    count = 1 
            
            # handle single digit
            output += str(count) + left

            return output 
        
        return sayNumber(self.countAndSay(n-1))
        
# @lc code=end

