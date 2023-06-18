# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> Optional[TreeNode]:
        idx = nums.index(max(nums))
        root = TreeNode(nums[idx])

        def traverse(node, arr, left):
            if not arr:
                return

            idx = arr.index(max(arr))
            if left:
                node.left = TreeNode(arr[idx])
                traverse(node.left, arr[:idx], True)
                traverse(node.left, arr[idx+1:], False)
            else:
                node.right = TreeNode(arr[idx])
                traverse(node.right, arr[:idx], True)
                traverse(node.right, arr[idx+1:], False)


        traverse(root, nums[:idx], True)
        traverse(root, nums[idx+1:], False)


        return root

class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> Optional[TreeNode]:
        def build(arr):
            if not arr:
                return 
            
            idx = arr.index(max(arr))
            node = TreeNode(arr[idx])
            node.left = build(arr[:idx])
            node.right = build(arr[idx+1:])
            
            return node

        return build(nums)