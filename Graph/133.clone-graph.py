#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node is None:
            return node
        # {oldNode : NewNode}
        oldToNew = {}
        
        def clone(node):
            # check if clone exist
            if node in oldToNew:
                return oldToNew[node]

            # create clone 
            copy = Node(node.val)
            oldToNew[node] = copy
            
            # clone neighbor
            for neigh in node.neighbors:
                copy.neighbors.append(clone(neigh))
                
            return copy 

        return clone(node)
                
                        
            
        
        
# @lc code=end

