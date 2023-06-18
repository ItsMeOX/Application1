from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.lis = []

        def traverse(node):
            if not node:
                return 
            traverse(node.left)
            self.lis.append(node.val)
            traverse(node.right)

        traverse(root)

        res = 10 ** 5
        for i in range(len(self.lis)-1):
            res = min(res, self.lis[i+1]-self.lis[i])
        
        return res

