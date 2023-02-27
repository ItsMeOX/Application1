# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [root]
        res = []
        temp = []
        x = 1
        y = 0

        if not root:
            return

        while q:
            for _ in range(x):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                    y += 1 
                if node.right:
                    q.append(node.right)
                    y += 1
                    
            res.append(temp)
            temp = []
            x = y
            y = 0
        
        return res


                




