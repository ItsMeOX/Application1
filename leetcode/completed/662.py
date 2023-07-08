from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque() # (node, idx)

        q.append((root, 0))

        res = 1
        while q:
            _, left_idx = q[0]
            _, right_idx = q[-1]
            res = max(res, right_idx - left_idx + 1)

            for _ in range(len(q)):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, idx * 2))
                if node.right:
                    q.append((node.right, idx * 2 + 1))

        return res


