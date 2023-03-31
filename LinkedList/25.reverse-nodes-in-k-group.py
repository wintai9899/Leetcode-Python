#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (54.52%)
# Likes:    10734
# Dislikes: 567
# Total Accepted:    674.7K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, reverse the nodes of the list k at a time,
# and return the modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in
# the end, should remain as it is.
# 
# You may not alter the values in the list's nodes, only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
# 
# 
# 
# Follow-up: Can you solve the problem in O(1) extra memory space?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        prevGroup = dummyNode

        while True:
            # kth = last element in the group to be reversed
            kthNode = self.getKthNode(prevGroup, k)

            # out of nodes
            if not kthNode:
                break
            
            nextGroup = kthNode.next 

            # reverse group 
            # prev cannot be set to None
            prev = kthNode.next
            cur = prevGroup.next 

            # reverse
            while cur != nextGroup:
                nextNode = cur.next
                cur.next = prev
                prev = cur
                cur = nextNode

            # make the links
            temp = prevGroup.next
            prevGroup.next = kthNode
            prevGroup = temp

        return dummyNode.next
    
    def getKthNode(self,cur,k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        
        return cur
        
# @lc code=end

