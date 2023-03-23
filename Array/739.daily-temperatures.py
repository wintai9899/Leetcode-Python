#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (66.32%)
# Likes:    10296
# Dislikes: 233
# Total Accepted:    589.6K
# Total Submissions: 889.3K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
# 
# 
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
# 
# 
# Constraints:
# 
# 
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                prevIdx, temp = stack.pop()
                res[prevIdx] = index - prevIdx
            
            stack.append((index,temperature))
        
        return res
        
# @lc code=end

