#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # lp     cur                             
        # 0   ->   1   ->   2   ->   3   ->   4   ->   5
        #                   L                 R
        dummyNode = ListNode(0, head)
        leftPrev = dummyNode
        cur = head 

        # Phase 1. move cur to left
        for _ in range(left - 1):
            leftPrev = cur 
            cur = cur.next
        
        #         lp       cur                             
        # 0   ->   1   ->   2   ->   3   ->   4   ->   5
        #                   L                 R
        
        # phase 2. Reverse from L to R
        prev = None
        for _ in range (right - left + 1):
            temp = cur.next
            cur.next = prev 
            prev = cur 
            cur = temp 

        #         lp                         prev     cur                             
        # 0   ->   1   ->   2   <-   3   <-   4   ->   5
        #                   L                 R
            

        # phase 3. clear up links 
        leftPrev.next.next = cur 
        leftPrev.next = prev

        return dummyNode.next
# @lc code=end

