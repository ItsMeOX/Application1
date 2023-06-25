from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if not root:
            return []
        else:
            q.append(root)
        res = []

        while q:
            max_ = -float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                max_ = max(max_, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(max_)
        
        return res
