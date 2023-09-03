from typing import Optional, List

# Perform backtracking and keep track of the sum of nodes value we have passed by.
# If we reach leaf node, check if sum of current path == targetSum, if yes then append.
# After having discovered all the leaf node, we pop current node value from 'path'.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                path.append(node.val)
                if sum(path) == targetSum:
                    res.append(path.copy())
                path.pop()
                return

            path.append(node.val)
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        
        res = []
        dfs(root, [])
        
        return res

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path: List[int]):
            if not node:
                return

            path.append(node.val)
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    res.append(path[:])

            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        
        res = []
        dfs(root, [])
        
        return res