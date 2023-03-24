#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (55.81%)
# Likes:    7760
# Dislikes: 222
# Total Accepted:    678.8K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subsets = []
        
        def backtrack(i):
            if i == len(nums):
                res.append(subsets.copy())
                return

            subsets.append(nums[i])
            backtrack(i+1)
            
            subsets.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
                
            backtrack(i+1)
        backtrack(0)

        return res
        
# @lc code=end

