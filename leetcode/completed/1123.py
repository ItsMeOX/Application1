from typing import Optional

# Perform DFS, 
# collect the maximum depth for the left and right child node for every node.
# 1. If left  depth == right depth, we have to include this node too.
# 2. If left  depth >  right depth, we will take the left child node.
# 3. If right depth >  left  depth, we will take the right child node.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, level):
            if not node:
                return None, level-1
            
            left_node, left_level = dfs(node.left, level+1)
            right_node, right_level = dfs(node.right, level+1)

            if left_level == right_level:
                return node, left_level
            elif left_level > right_level:
                return left_node, left_level
            else:
                return right_node, right_level
            
        res, _ = dfs(root, 0)
        
        return res