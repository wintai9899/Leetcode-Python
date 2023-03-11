#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # pair : (index, height)
        stack = []
        maxArea = 0

        # key point: we can extend the width if the histograms is in increasing order
        for i,h in enumerate(heights):
            start = i 
            # cur h > prev h: need to pop from stack
            while stack and h < stack[-1][1]:
                prevIndex, prevHeight = stack.pop()
                # compute max height
                width = i - prevIndex
                area = width * prevHeight
                maxArea = max(maxArea, area)
                # extend the rectangle backwards to achieve max area
                start = prevIndex
            stack.append((start, h))
            
        # if the stack is not empty, we can still find more potential results 
        # theses entries can extend to the end of the histograms, so the width =  len(heights) - i
        for i,h in stack:
            width = len(heights) - i
            maxArea = max(maxArea, h * width)
        
        return maxArea
        
# @lc code=end

