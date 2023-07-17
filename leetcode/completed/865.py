from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# my approach:
# use BFS to traverse can store leaf nodes in a list,
# in the process of traversing, store the parent of node in that node.
# After done scanning through the tree and getting the leaf nodes,
# start traversing from each leaf node and count the node they traversed along the way.
# if all the leaf nodes passed through a node, that node will be the first node containing all the deepest nodes,
# that first node will be our answer.

# time complexity : O(n)
# space complexity: O(n)

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        q = deque()
        q.append((root, None)) # node, prev
        leaves = []

        while q:
            leaves.clear()
            for _ in range(len(q)):
                node, prev = q.popleft()
                node.prev = prev
                leaves.append(node)
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

        count = len(leaves)
        counter = {}
        for leaf in leaves:
            while leaf:
                counter[leaf] = counter.get(leaf, 0) + 1
                leaf = leaf.prev

        for key in counter.keys():
            if counter[key] == count:
                return key
            
# another approach:

# Start a dfs at root,
# keep traversing until the root node.

# We will choose the deepest subtree.
# For every node, if depth of left subtree > depth of right subtree, then we return left subtree,
# if depth of left subtree < depth of right subtree, then we return right subtree
# else, we return current node. 

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (0, None)
            
            left, right = dfs(node.left), dfs(node.right)

            if left[0] < right[0]:
                return (right[0]+1, right[1])
            elif left[0] > right[0]:
                return (left[0]+1, left[1])
            else:
                return (left[0]+1, node)
        
        return dfs(root)[1]