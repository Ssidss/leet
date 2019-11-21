# _*_ coding: utf-8 _*_

"""
114. Flatten Binary Tree to Linked List
Medium
Given a binary tree, flatten it to a linked list in-place.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        stack = [root.right, root.left]
        prev = root
        while stack:
            cur_node = stack.pop()
            if cur_node: 
                prev.left, prev.right, prev = None, cur_node, cur_node
                stack.extend([cur_node.right, cur_node.left])
        return root

