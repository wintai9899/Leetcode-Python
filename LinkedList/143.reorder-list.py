#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (52.35%)
# Likes:    8409
# Dislikes: 287
# Total Accepted:    648.2K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
# 
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# 
# Reorder the list to be on the following form:
# 
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# 
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. find midpoint of ll
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. reverse second portion of ll
        secondHalf = slow.next
        prev = slow.next = None
        
        while secondHalf:
            tempNode = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = tempNode
        
        # 3. Merge two ll 
        first = head 
        second = prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second 
            second.next = temp1
            
            first = temp1
            second = temp2
        
        
# @lc code=end

