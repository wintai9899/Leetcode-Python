#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    # greedy approach
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = nums[0]
        
        for num in nums[1:]:
            curSum = max(curSum + num, num)
            maxSum = max(curSum, maxSum)
        
        return maxSum
    
    # sol2
    def maxSubArray2(self,nums):
        maxSub = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
                
            curSum += n
            maxSub = max(maxSub, curSum)
        
        return maxSub
# @lc code=end

