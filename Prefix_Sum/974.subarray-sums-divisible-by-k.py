#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dp = {0 : 1}
        prefixSum = 0
        res = 0
        
        for num in nums:
            prefixSum += num
            key = prefixSum % k
            
            if key in dp:
                res += dp[key]
                dp[key] += 1
            else:
                dp[key] = 1
        
        return res
        
# @lc code=end

