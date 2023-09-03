# Pre-order : Discover current node before leaf nodes
# In-order  : Flatten the tree
# Post-order: Discover leaf nodes before current node



from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node, skip):
            if not node:
                return 0

            if (node, skip) in memo:
                return memo[(node, skip)]

            if not skip:
                left = max(dfs(node.left, False), dfs(node.left, True))
                right = max(dfs(node.right, False), dfs(node.right, True))
                res = left + right
                res = max(res, dfs(node.left, True) + dfs(node.right, True) + node.val) 

                memo[(node, skip)] = res

                return memo[(node, skip)]
            else:
                left = dfs(node.left, False)
                right = dfs(node.right, False)
                memo[(node, skip)] = left + right
                return memo[(node, skip)]

        return max(dfs(root, False), dfs(root, True))



# Do a post-order traversal.
# Every recursion, we will return (val if not skipping, val if skipping).
# If we do not skip, then we must take return[1],
# if we skip, we will take sum of max of left and max of right.
# If current node is null, just return 0.

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            not_skip = node.val + left[1] + right[1]
            skip = max(left) + max(right)

            return (not_skip, skip)

        return max(dfs(root))