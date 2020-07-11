"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l =[]
        while head:
            l.append(head.val)
            head = head.next
        i, j = 0, len(l)-1
        while i < j:
            if l[i]==l[j]:
                i+=1
                j-=1
            else:
                return False
        return True