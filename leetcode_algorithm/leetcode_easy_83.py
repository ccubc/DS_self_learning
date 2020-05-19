"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        if not head:
            return head
        while cur.next:
            if cur.val != cur.next.val:
                cur = cur.next
            else:
                cur.next = cur.next.next
        return head



class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        if not head:
            return head
        while cur.next:
            nxt = cur.next
            if cur.val == nxt.val:
                cur.next = nxt.next
                continue
            cur = cur.next
        return head