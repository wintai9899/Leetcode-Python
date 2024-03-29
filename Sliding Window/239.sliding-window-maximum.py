#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (46.34%)
# Likes:    13991
# Dislikes: 458
# Total Accepted:    739K
# Total Submissions: 1.6M
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
# 
# Return the max sliding window.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = [] 
        # Monotonic Q : -> decreasing order
        # first element on the left is always the largest 
        q = collections.deque() # indices not values
        l,r = 0,0 

        while r < len(nums):
            # keep removing elements if nums[r] is large
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # q[0] will always be the largest in the q
            # maintain window
            # prev window max is still the largest in the current window 
            if l > q[0]:
                q.popleft()
            
            if (r - l + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
    
        return output


        
# @lc code=end

