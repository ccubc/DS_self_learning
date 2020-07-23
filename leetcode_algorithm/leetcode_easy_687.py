"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

 

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
class Solution:   
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest = 0
        
        def dfs(node):
            if not node:
                return 0          
            left, right = dfs(node.left), dfs(node.right)
            left_path = left + 1 if node.left and node.val==node.left.val else 0
            right_path = right + 1 if node.right and node.val==node.right.val else 0
            self.longest = max(self.longest, left_path + right_path)
            return max(left_path, right_path)
        
        dfs(root)
        return self.longest
        