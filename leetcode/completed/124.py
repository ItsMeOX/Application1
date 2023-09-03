from typing import Optional

# For every node, perform a post traversal (collect sum of value of child nodes first).
# If either value is negative, then we will just discard the subtree.
# Compare res with left path + current node + right path.
# Because that our route cannot be splitted, we have to decide left or right subtree to choose as path,
# so we will choose the largest value path and return largest value path + node.val .

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            nonlocal res

            if not node: return 0

            left = max(dfs(node.left), 0)

            right = max(dfs(node.right), 0)

            res = max(res, left+right+node.val)

            return max(left, right) + node.val

        res = -float('inf')
        dfs(root)

        return res