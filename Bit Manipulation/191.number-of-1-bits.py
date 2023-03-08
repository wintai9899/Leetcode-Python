#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n != 0:
            res += 1
            # remove the rightmost 1 from n
            n = n & (n-1)
        
        return res
        
# @lc code=end

