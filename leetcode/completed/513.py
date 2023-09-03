from typing import Optional
from collections import deque

# Perform BFS and for every first node in every level, overwrite res with 'node.val'.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0: res = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
        return res
    

# Also BFS, but explore from right to level for every level.class Solution:
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q = deque([root])

        while q:
            node = q.popleft()

            res = node.val

            if node.right: q.append(node.right)

            if node.left: q.append(node.left)
            
        return res