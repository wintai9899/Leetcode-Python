#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (46.31%)
# Likes:    10133
# Dislikes: 179
# Total Accepted:    606.8K
# Total Submissions: 1.3M
# Testcase Example:  '[1,5,11,5]'
#
# Given an integer array nums, return true if you can partition the array into
# two subsets such that the sum of the elements in both subsets is equal or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # not possible if odd
        if sum(nums) % 2 != 0:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1,-1,-1):
            nextDp = set()
            for t in dp:
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp

        return True if target in dp else False
        
# @lc code=end

