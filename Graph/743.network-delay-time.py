#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adjacency list {src_node : [weight, targetNode]}
        graph = collections.defaultdict(list)
        for src, dest, weight in times:
            graph[src].append([weight, dest])
        # start with K as source node
        # (path_length, node)
        minHeap = [(0,k)]
        heapq.heapify(minHeap)
        visited = set() 
        # cost to visit node
        time = 0 

        while minHeap:
            curWeight, curNode = heapq.heappop(minHeap)
            if curNode in visited:
                continue
            visited.add(curNode)
            time = max(time, curWeight)

            # get neighbors
            for neiWeight, neiNode in graph[curNode]:
                if neiNode not in visited:
                    newWeight = curWeight + neiWeight
                    heapq.heappush(minHeap, (newWeight, neiNode))
        
        return time if len(visited) == n else -1
        
# @lc code=end

