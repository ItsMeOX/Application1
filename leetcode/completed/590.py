from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []

        def dfs(node):
            for child in node.children:
                dfs(child)
            res.append(node.val)

        res = []
        dfs(root)
        return res