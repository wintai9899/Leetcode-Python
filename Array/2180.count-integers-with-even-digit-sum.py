#
# @lc app=leetcode id=2180 lang=python3
#
# [2180] Count Integers With Even Digit Sum
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        res = 0 
        for n in range(1,num + 1):
            if self.getDigitSum(n) % 2 == 0:
                res += 1
        
        return res
    
    def getDigitSum(self,num):
        s = str(num)
        digitSum = 0
        for digit in s:
            digitSum += int(digit)
            
        return digitSum
            
        
            
        
# @lc code=end

