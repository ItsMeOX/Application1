from typing import List, Optional

# If n = 3, then arr = [1,2,3]
# We iterate i from 1 to 3,
# i will be the current node, [left, i-1] will be left subtree, [i+1, right] will be right subtree.
#
# if left == right, we will return [TreeNode(left)] or [TreeNode(right)],
#
# if left > right, we will return [], but if we return [], 
# for example, left_children: [] and right_children: [2,3], it will not append right child to current node as left_children is empty and no loop will occur,
# so we have to append 'None' to left children.
# This is also the same for right_child.
#
# After collecting left and right children, 
# we pair left and right children one by one and append them to current node, then add current node to 'res'.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(left, right):
            if left == right:
                return [TreeNode(left)]
            
            res = []
            for i in range(left, right+1):
                left_children = dfs(left, i-1) or [None]
                right_children = dfs(i+1, right) or [None]
                for left_child in left_children:
                    for right_child in right_children:
                        node = TreeNode(i)
                        node.left = left_child
                        node.right = right_child
                        res.append(node)
            
            return res

        return dfs(1, n)