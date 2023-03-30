#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (63.97%)
# Likes:    3466
# Dislikes: 84
# Total Accepted:    154K
# Total Submissions: 240.7K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].
# 
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
# absolute value of val.
# 
# Return the minimum cost to make all points connected. All points are
# connected if there is exactly one simple path between any two points.
# 
# 
# Example 1:
# 
# 
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 
# 
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
# 
# 
# 
# Constraints:
# 
# 
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# All pairs (xi, yi) are distinct.
# 
# 
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i : [] for i in range(len(points))}
        
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
                
        res = 0
        minHeap = [[0,0]]
        heapq.heapify(minHeap)
        visited = set()
        
        while len(visited) < len(points):
            curCost, curPoint = heapq.heappop(minHeap)
            
            if curPoint in visited:
                continue
            
            res += curCost
            visited.add(curPoint)
            
            for neiCost, neiPoint in adj[curPoint]:
                if neiPoint not in visited:
                    heapq.heappush(minHeap, [neiCost, neiPoint])
        
        return res
        
# @lc code=end

