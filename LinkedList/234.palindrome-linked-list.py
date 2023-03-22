#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (50.13%)
# Likes:    13406
# Dislikes: 741
# Total Accepted:    1.4M
# Total Submissions: 2.8M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
# 
# 
# 
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get mid point 

        # 1   ->    2    ->    2    ->    1

        slow = fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #                     S                   F
        # 1   ->    2    ->    2    ->    1   -> None
        
        # reverse from slow to fast
        prev = None
        while  slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp 

        #                             prev    S                           
        # 1   ->    2    ->    2   <-  1   -> None

        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next
        
        return True
        
# @lc code=end

