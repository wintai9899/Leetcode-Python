#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (52.06%)
# Likes:    16729
# Dislikes: 306
# Total Accepted:    1.2M
# Total Submissions: 2.3M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """                                     
                 0     1     2     3      4     5
       nums [    0,    1,    0,    3,     2,    3    ]  
       
       dp = [    1,    1,    1,    1,     1,    1    ]  
       
       dp = lengths of increasing subsequences
     
       dp[5] = max(dp[5], 1 + dp[6] if nums[5] < nums[6]) = dp[5] = 1 
       dp[4] = max(dp[4], 1 + dp[5]) = max(1,2) = 2 
       dp[3] = max(dp[3]) = 1   # nothing on the right side of nums[3] is larger than nums[3]
       dp[2] = max(dp[2], 1 + dp[3], 1 + dp[4], 1 + dp[5]) = max(1, 3) = 3  # only nums[3], nums[4] and nums[5] is larger tan nums[2]
       dp[1] = max(dp[1], 1 + dp[3], 1 + dp[4], 1 + dp[5]) = max(1, 2) = 3
       
       dp[0] = max(dp[0], 1 + dp[1], 1 + dp[3], 1 + dp[2], 1 + dp[5]) = max(1, 1 + dp[1]) = 4
       
        """
        
        dp = [1] * len(nums)
        
        # traverse from the end
        for i in range(len(nums)-1,-1,-1):
            # traverse the right subarray of nums[i]
            for j in range(i+1,len(nums)):
                # add to longest sub array
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)
        
# @lc code=end

