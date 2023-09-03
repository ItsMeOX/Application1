# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_array = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            sorted_array.append(node.val)
            dfs(node.right)
        
        dfs(root)

        def build(arr):
            if not arr:
                return
            
            mid = len(arr) // 2

            root = TreeNode(arr[mid])
            root.left = build(arr[:mid])
            root.right = build(arr[mid+1:])
            
            return root
        
        return build(sorted_array)
    
# Perform a inorder traversal and get the sorted values from root.
# After getting the sorted-value array,
# We build the tree by using the middle-indexed value as current node,
# and the left part of the array [left, mid) will be the left subtree of current node,
# and the right part of the array (mid, right] will be the right subtree of current node.
# If we reach [left, right) where left == right, then this means that the array is empty, so just return.

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_array = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            sorted_array.append(node.val)
            dfs(node.right)
        
        dfs(root)

        def build(left, right): # [left, right)
            if left == right:
                return
            
            mid = (left+right) // 2

            root = TreeNode(sorted_array[mid])
            root.left = build(left, mid)
            root.right = build(mid+1, right)
            
            return root
        
        return build(0, len(sorted_array))