#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (49.70%)
# Likes:    16664
# Dislikes: 607
# Total Accepted:    1.6M
# Total Submissions: 3.2M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
# 
# Example 1:
# 
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# 
# 
# Example 2:
# 
# 
# Input: lists = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: lists = [[]]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # error checking
        if len(lists) == 0:
            return None

        # merge 2 lists at a time 
        while len(lists) > 1:
            mergedList = []
            for i in range(0,len(lists),2):
                l1 = lists[i] 
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedList.append(self.mergeTwoLists(l1,l2))
            # copy mergedList to current list
            lists = mergedList
        
        return lists[0]

    def mergeTwoLists(self, list1,list2):
        res = ListNode(None)
        tail = res 

        while list1 and list2:
            val1 = list1.val if list1 else None
            val2 = list2.val if list2 else None 

            if val1 < val2:
                tail.next = ListNode(val1)
                list1 = list1.next

            else:
                tail.next = ListNode(val2)
                list2 = list2.next 
            
            tail = tail.next 

        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2

        return res.next
        


# @lc code=end

