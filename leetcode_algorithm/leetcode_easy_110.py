"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

Accepted
450,570
Submissions
1,038,753
Seen this question in a real interview before?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, root):
        if not root:
            return 0
        else: return max(self.getDepth(root.left), self.getDepth(root.right)) + 1
        
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: 
            return True
        return abs(self.getDepth(root.right) - self.getDepth(root.left))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)