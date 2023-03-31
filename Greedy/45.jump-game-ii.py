#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (39.80%)
# Likes:    11963
# Dislikes: 418
# Total Accepted:    865.5K
# Total Submissions: 2.2M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
# 
# Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i +
# j] where:
# 
# 
# 0 <= j <= nums[i] and
# i + j < n
# 
# 
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,3,0,1,4]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
# 
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # nums = [2,  3,  1,  1,   4]
        # think what is the furthest current nums[i] can jump
        # [2,  3,  1,  1,   4]
        #  A   <-B->   <- C->
        #  0     1        2
        # the furthest jump for A will land in Subarray b
        # the furthest jump from subarray b is to c 
        # think of it like a bfs: 2 -> [3,1] region -> [1,4] region  : 2 jumps

        # [2,  3,  1,  1,   4]
        #  A   <-B->   <- C->
        #      L    R        
        
        # [2,  3,  1,  1,   4]
        #  A   <-B->   <- C->
        #              L     R


        res = 0
        # window of current subarray
        l,r = 0,0
        # BFS
        while r < len(nums)-1:
            furthestJump = 0
            # find furthest jump in current subarray
            for i in range(l,r+1):
                furthestJump = max(furthestJump, nums[i] + i)

            # shift pointers 
            l = r 
            r = furthestJump 

            res += 1
        
        return res

        
# @lc code=end

