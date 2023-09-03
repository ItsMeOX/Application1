from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node, visited):
            if not node.left and not node.right:
                res.append('->'.join(visited))
                return
            
            if node.left:
                visited.append(str(node.left.val))
                dfs(node.left, visited)
                visited.pop()
            
            if node.right:
                visited.append(str(node.right.val))
                dfs(node.right, visited)
                visited.pop()


        res = []
        dfs(root, [str(root.val)])
        return res

# Optimization:
# Using string instead of list.

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node, path):
            path += str(node.val)

            if not node.left and not node.right:
                res.append(path)
                return
            
            if node.left:
                dfs(node.left, path + '->')
            
            if node.right:
                dfs(node.right, path + '->')

        res = []
        dfs(root, '')
        return res