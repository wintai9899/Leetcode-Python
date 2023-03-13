#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = {0 : 1}
        res, preSum = 0,0 
        
        for num in nums:
            preSum += num
            diff = preSum - k 
            
            res += dp.get(diff,0)
            
            dp[preSum] = dp.get(preSum,0) +1 
        
        return res
# @lc code=end

