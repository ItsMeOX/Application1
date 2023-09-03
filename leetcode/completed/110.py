from typing import Optional

# If abs(depth_left - depth_right) > 1, then return -1.
# Else, return maximum depth between left and right.
# Using -1 as signal, if dfs returns -1, it means res = False, so return -1 all the way.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return dfs(root) != -1
        

            