"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        elif root.left and root.right:
            return [(str(root.val)+"->"+i) for i in self.binaryTreePaths(root.left)]+[(str(root.val)+"->"+i) for i in self.binaryTreePaths(root.right)]
        elif root.left:
            return [(str(root.val)+"->"+i) for i in self.binaryTreePaths(root.left)]
        elif root.right:
            return [(str(root.val)+"->"+i) for i in self.binaryTreePaths(root.right)]
        else:
            return [str(root.val)]