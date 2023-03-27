#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (40.63%)
# Likes:    16842
# Dislikes: 754
# Total Accepted:    1.3M
# Total Submissions: 3.2M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
# 
# Implement the LRUCache class:
# 
# 
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# 
# 
# The functions get and put must each run in O(1) average time complexity.
# 
# 
# Example 1:
# 
# 
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
# 
# 
#

# @lc code=start
class Node:
    def __init__(self,key,val):
      self.key = key
      self.val = val
      self.next = None
      self.prev = None 
      
class LRUCache:
    # cache : {key : pointer to node in doubly linked list}
    # [LRU] <-> [key1,val1] <-> [key2,val2] <-> [MRU]
    def __init__(self, capacity: int):
      self.capacity = capacity
      self.cache = {}
      # left = Least Recent Used
      self.leftNode = Node(0,0)
      # right = Most Recent Used
      self.rightNode = Node(0,0)
      
      #[LRU] <-> [MRU]
      self.leftNode.next = self.rightNode
      self.rightNode.prev = self.leftNode
      

    def get(self, key: int) -> int:
        # check if exist
        if key in self.cache:
          # move to MRU
          self.remove(self.cache[key])
          self.insert(self.cache[key])
          return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
          # move to MRU
          self.remove(self.cache[key])
        # insert into cache
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        # remove least recent used
        if len(self.cache) > self.capacity:
            LRU = self.leftNode.next
            self.remove(LRU)
            del self.cache[LRU.key]
          
        
    def remove(self, node):
  
        prevNode = node.prev
        nextNode = node.next
        
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def insert(self,node):
        prevNode = self.rightNode.prev
        nextNode = self.rightNode 

        prevNode.next = node
        node.prev = prevNode
        node.next = nextNode
        nextNode.prev = node
      
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

