from heapq import heappop, heappush

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        heap = []

        def dfs(node):
            if not node:
                return 0

            res = 1 if not heap or -heap[0] <= node.val else 0

            if not heap or -heap[0] <= node.val:
                heappush(heap, -node.val)

            res += dfs(node.left)
            res += dfs(node.right)

            if -heap[0] == node.val:
                heappop(heap)

            return res

        return dfs(root)
    
# Perform a preorder dfs on tree.
# During the traversal, we keep track of current 'greatest'.
# If greatest <= current node value, set 'res' to 1, else set 'res' to 0.
# Add result from left and right child to 'res'.
# If dfs reached null node, return 0.
# Return 'res' at last.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, greatest):
            if not node:
                return 0

            if greatest <= node.val:
                res = 1
                greatest = node.val
            else:
                res = 0
            
            res += dfs(node.left, greatest)
            res += dfs(node.right, greatest)

            return res

        return dfs(root, -float('inf'))