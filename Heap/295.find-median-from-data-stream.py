#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (51.45%)
# Likes:    10033
# Dislikes: 196
# Total Accepted:    620.2K
# Total Submissions: 1.2M
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value, and the median is the mean of the two
# middle values.
# 
# 
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# 
# 
# Implement the MedianFinder class:
# 
# 
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data
# structure.
# double findMedian() returns the median of all elements so far. Answers within
# 10^-5 of the actual answer will be accepted.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# 
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# 
# 
# 
# Constraints:
# 
# 
# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling
# findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are in the range [0, 100], how would
# you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how
# would you optimize your solution?
# 
# 
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        # eg. data = [1,2,3,4,5,6,7]
        #                                      max
        # firstHalf (smaller values)  = [1,2,3,4] = [-4,-3,-2,-1] (maxHeap)
        #                               min
        # second half (larger values) = [5,6,7] (minHeap)
        # compare max(firstHalf) and min(secondHalf) to get median

        self.firstHalf = []  # smaller values
        self.secondHalf = [] # larger values


        
    def addNum(self, num: int) -> None:
        # default: add to firstHalf (-1 for maxHeap)
        heapq.heappush(self.firstHalf, -1 * num)

        # check: every value in first half must smaller than every value in secondhalf
        if self.firstHalf and self.secondHalf:
            maxValueFromFirst = -1 * self.firstHalf[0]
            minValueFromSecond = self.secondHalf[0]
            
            # add to secondHalf
            if maxValueFromFirst > minValueFromSecond:
                firstMax = -1 * heapq.heappop(self.firstHalf)
                heapq.heappush(self.secondHalf, firstMax)
        
        # balance the length of both heaps

        if len(self.firstHalf) > len(self.secondHalf) + 1:
            val = -1 * heapq.heappop(self.firstHalf)
            heapq.heappush(self.secondHalf, val)
        
        if len(self.secondHalf) > len(self.firstHalf) + 1:
            val = heapq.heappop(self.secondHalf)
            heapq.heappush(self.firstHalf, -1 * val)
        
    def findMedian(self) -> float:
        # median = max from firstHalf + min from secondHalf // 2

        # uneven size
        if (len(self.firstHalf) > len(self.secondHalf)):
            return -1 * self.firstHalf[0]
        
        if (len(self.secondHalf) > len(self.firstHalf)):
            return self.secondHalf[0]
        
        return (-1*self.firstHalf[0] + self.secondHalf[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

