#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(None)
        tail = res 
        carry = 0 
        
        while l1 or l2 or carry: 
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 
            
            output = val1 + val2 + carry
            # eg. outp = 13 -> carry:1, digit:3
            carry, digit = divmod(output,10)
            
            tail.next = ListNode(digit)
            tail = tail.next 
            
            if l1:
                l1 = l1.next 
            
            if l2:
                l2 = l2.next 
        
        return res.next
            
        
# @lc code=end

