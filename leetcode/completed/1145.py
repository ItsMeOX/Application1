from typing import Optional

#       1
#      / \
#     2   3
#    / \
#   4   5
# x = 1.
# To win, we have to make sure that the amount of nodes covered by us will be > n / 2.
# We have to check if 
# 1. amount of left subtree of node x > n / 2,
# 2. amount of right subtree of node x > n / 2,
# 3. amount of parent tree excluding x and its child node > n / 2.
# If any is true then there is always a way that y will have more amount of nodes than x.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        def dfs(node):
            nonlocal left, right
            if not node: return 0

            l = dfs(node.left)
            r = dfs(node.right)

            if node.val == x:
                left = l
                right = r
            
            return l+r+1

        left = right = 0
        dfs(root)

        return left*2 > n or right*2 > n or (n-left-right-1)*2 > n