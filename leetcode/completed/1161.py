from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = {}

        def dfs(node, level):
            if not node:
                return
            
            level_sum[level] = level_sum.get(level, 0) + node.val

            dfs(node.left, level+1)
            dfs(node.right, level+1)
            
        dfs(root, 1)

        return max(level_sum, key=level_sum.get)
    
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        max_sum = -10 ** 5
        max_level = 0
        level = 0
        while q:
            level += 1
            _sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                _sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if _sum > max_sum:
                max_sum = _sum
                max_level = level
            
        return max_level