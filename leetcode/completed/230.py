from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            sorted_list.append(node.val)
            dfs(node.right)

        dfs(root)
    
        return sorted_list[k-1]
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        node = root 

        while (stack or node):
            while node:
                stack.append(node)
                node = node.left

            k -= 1
            node = stack.pop()
            if k == 0:
                return node.val
            
            node = node.right

        return 0