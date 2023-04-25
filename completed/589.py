"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.res = list()
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return None
        self.dfs(root)
        return(self.res)

    def dfs(self, root):
        self.res.append(root.val)
        for child in root.children:
            self.dfs(child)
            
            