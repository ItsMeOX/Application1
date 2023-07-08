from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, sum):
            if not node:
                return False, None
            if not node.left and not node.right:
                if sum+node.val < limit:
                    return False, None
                else:
                    return True, node
            

            leftSuff, leftChild = dfs(node.left, sum+node.val)
            rightSuff, rightChild = dfs(node.right, sum+node.val)

            node.left = leftChild
            node.right = rightChild

            if not leftSuff and not rightSuff:
                return False, None

            return True, node
            
        _, node = dfs(root, 0)
        return node
    
    
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, path_sum):
            if not node:
                return False

            path_sum += node.val

            if not node.left and not node.right:
                return path_sum >= limit

            left = dfs(node.left, path_sum)
            right = dfs(node.right, path_sum)

            if not left:
                node.left = None
            if not right:
                node.right = None

            return left or right

        res = dfs(root, 0)
        return root if res else None