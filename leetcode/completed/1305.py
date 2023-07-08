from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = list()

        def dfs(node):
            if not node:
                return

            res.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root1)
        dfs(root2)

        return sorted(res)
    

from collections import deque
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = list()
        q1, q2 = deque(), deque()

        def dfs(node, q):
            if not node:
                return
            
            dfs(node.left, q)
            q.append(node.val)
            dfs(node.right, q)
        
        dfs(root1, q1)
        dfs(root2, q2)

        while q1 and q2:
            if q1[0] > q2[0]:
                res.append(q2.popleft())
            else:
                res.append(q1.popleft())

        while q1:
            res.append(q1.popleft())
        while q2:
            res.append(q2.popleft())

        return res