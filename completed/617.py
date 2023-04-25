# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:        
        if not root1:
            return root2
        if not root2:
            return root1

        def dfs(root1, root2):
            if not root1:
                return True
            if not root2:
                return
            root1.val += root2.val


            if dfs(root1.left, root2.left):
                root1.left = root2.left
            if dfs(root1.right, root2.right):
                root1.right = root2.right

        dfs(root1, root2)
        return root1


# class Solution:
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:        
#         if not root1:
#             return root2
#         if not root2:
#             return root1

#         res = TreeNode(root1.val + root2.val)
#         res.left = self.mergeTrees(root1.left, root2.left)
#         res.right = self.mergeTrees(root1.right, root2.right)


#         return res