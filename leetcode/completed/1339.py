from typing import Optional

# Get sums of every node + node.val for every node,
# then for every node, compare res with sum(total - child node) * (child node).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        MOD = 10 ** 9 + 7
        sums = {}

        def dfs(node):
            if not node: return 0

            sums[node] = dfs(node.left) + dfs(node.right) + node.val

            return sums[node]
        dfs(root)        

        def dfs2(node):
            if not node: return 0

            res = 0
            if node.left:
                res = max(res, sums[node.left] * (sums[root] - sums[node.left]))

            if node.right:
                res = max(res, sums[node.right] * (sums[root] - sums[node.right]))

            return max(res, dfs2(node.left), dfs2(node.right))

        return dfs2(root) % MOD
    
# Optimization: 
# instead of using another dfs, we can store sums in an array instead of a dictionary,
# and iterate through the array and get the product for every node.

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        MOD = 10 ** 9 + 7
        sums = []

        def dfs(node):
            if not node: return 0
            sums.append(dfs(node.left) + dfs(node.right) + node.val)
            return sums[-1]
        total = dfs(root)
        res = 0

        for val in sums:
            res = max(res, val * (total - val))
        
        return res % MOD