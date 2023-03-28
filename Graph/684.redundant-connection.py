#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (62.20%)
# Likes:    5092
# Dislikes: 347
# Total Accepted:    266.8K
# Total Submissions: 428.8K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
# 
# You are given a graph that started as a tree with n nodes labeled from 1 to
# n, with one additional edge added. The added edge has two different vertices
# chosen from 1 to n, and was not an edge that already existed. The graph is
# represented as an array edges of length n where edges[i] = [ai, bi] indicates
# that there is an edge between nodes ai and bi in the graph.
# 
# Return an edge that can be removed so that the resulting graph is a tree of n
# nodes. If there are multiple answers, return the answer that occurs last in
# the input.
# 
# 
# Example 1:
# 
# 
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# 
# 
# Example 2:
# 
# 
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
# 
# 
# 
# Constraints:
# 
# 
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
# 
# 
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # UNION FIND
        # init: each node is parent of its own
        #[0, 1, 2, 3, 4]
        parents = [i for i in range(len(edges)+1)]

        # size of graph - init: each node is an independent
        # [1, 1, 1, 1, 1]
        rank = [1] * (len(edges)+1)
        
        # find the parent
        def find(node):
            res = node

            while res != parents[res]:
                # optimization: connect to grandparent it exists, to prevent creation of linked list
                parents[res] = parents[parents[res]]
                res = parents[res]
            
            return res
        
        def union(node1,node2):
            # get parents of both nodes
            p1 = find(node1)
            p2 = find(node2)

            # if same parent: (already in the same graph)
            if p1 == p2:
                return 0

            # compare the rank of both 
            # smaller rank merge to large rank
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
               
            else: 
                parents[p1] = p2
                rank[p2] += rank[p1]
                
           
            return 1
        
        
        for n1,n2 in edges:
            if union(n1,n2) == 0:
                return [n1,n2]
        
       