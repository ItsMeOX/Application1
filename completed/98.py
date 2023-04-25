# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf = sys.maxsize
        def check(root, lower, upper):
            if not root:
                return True
            
            if lower < root.val < upper:
                return check(root.left, lower, root.val) and check(root.right, root.val, upper)

            
            return False
        
        return check(root, -inf, inf)