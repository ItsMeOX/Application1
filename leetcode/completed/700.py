from typing import Optional

# Traverse throught the BST tree. 
# If current node's val is > val, it means we have to search lower, so recurse left.
# Else if current node's val is < val, it means we have to search higher, so recurse right.
# Else, current node's val is = val, then we have found the node we want, so just return the node.
# Time: O(H)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return root