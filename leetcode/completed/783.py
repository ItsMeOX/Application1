from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        lis = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            lis.append(node.val)
            dfs(node.right)

        dfs(root)

        res = lis[-1] - lis[0]
        for i in range(1, len(lis)):
            res = min(res, lis[i]-lis[i-1])

        return res

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        prev = -1
        def dfs(node):
            nonlocal prev,  res
            if not node:
                return
            dfs(node.left)
            if prev != -1:
                res = min(res, node.val - prev)
            prev = node.val
            dfs(node.right)

        dfs(root)

        return res
