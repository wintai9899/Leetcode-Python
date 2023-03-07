#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort according to start 
        intervals.sort(key = lambda x : x[0])
        output = [intervals[0]]
        
        for start,end in intervals[1:]:
            prevEnd = output[-1][1]
            
            if start <= prevEnd:
                output[-1][1] = max(prevEnd, end)
            
            else:
                output.append([start,end])
        
        return output
        
# @lc code=end

