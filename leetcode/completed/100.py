from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root: return ''
            res = ''
            dq = deque([root])
            while dq:
                node = dq.popleft()
                if node == ' ':
                    res += ' '
                    continue
                res += str(node.val)

                if node.left:
                    dq.append(node.left)
                else:
                    dq.append(' ')
                if node.right:
                    dq.append(node.right)
                else:
                    dq.append(' ')
                
            return res

        return dfs(p) == dfs(q)
    
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if (not p and q) or (not q and p) or p.val != q.val: # if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
