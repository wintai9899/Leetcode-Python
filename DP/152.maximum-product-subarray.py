#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (34.87%)
# Likes:    15484
# Dislikes: 467
# Total Accepted:    972.6K
# Total Submissions: 2.8M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a subarray that has the largest product,
# and return the product.
# 
# The test cases are generated so that the answer will fit in a 32-bit
# integer.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = 1
        curMin = 1
        
        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
                continue 
            
            temp = n * curMax 
            curMax = max(temp, n * curMin, n)
            curMin = min(temp, n * curMin ,n)
        
            res = max(res, curMax)
        
        return res
        
# @lc code=end

