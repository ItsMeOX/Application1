from typing import Optional

# Base case: if node == null, return 0.
# Traverse to left and right child nodes first,
# for every node, 
# if prev node val == curr node val, return 1 + max(left, right),
# else return 0.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node, prev):
            nonlocal res
            if not node: return 0

            left = dfs(node.left, node)
            right = dfs(node.right, node)

            res = max(res, left + right)

            if prev.val != node.val:
                return 0
            else:
                return max(left, right) + 1

        res = 0
        dfs(root, root)
        return res