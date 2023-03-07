#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = nums[0]
        
        for num in nums[1:]:
            curSum = max(curSum + num, num)
            maxSum = max(curSum, maxSum)
        
        return maxSum
        
# @lc code=end

