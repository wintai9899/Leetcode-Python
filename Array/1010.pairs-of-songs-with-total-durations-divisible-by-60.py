#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Medium (52.78%)
# Likes:    3804
# Dislikes: 147
# Total Accepted:    236.5K
# Total Submissions: 448K
# Testcase Example:  '[30,20,150,100,40]'
#
# You are given a list of songs where the i^th song has a duration of time[i]
# seconds.
# 
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60. Formally, we want the number of indices i, j such that i
# < j with (time[i] + time[j]) % 60 == 0.
# 
# 
# Example 1:
# 
# 
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# 
# 
# Example 2:
# 
# 
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible
# by 60.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= time.length <= 6 * 10^4
# 1 <= time[i] <= 500
# 
# 
#

# @lc code=start
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0 
        remainders = collections.defaultdict(int)
        
        for t in time:
            if t % 60 == 0:
                res += remainders[0]
            
            else:
                res += remainders[60 - t % 60]
            
            remainders[t % 60] += 1
        
        return res
        
# @lc code=end

