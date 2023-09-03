from typing import Optional

# TC: O(N) for init, O(1) for next and hasNext.
# SC: O(N)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.dfs(root)
        self.pointer = 0

    def dfs(self, node: Optional[TreeNode]) -> None:
        if not node:
            return
        
        self.dfs(node.left)
        self.arr.append(node.val)
        self.dfs(node.right)

    def next(self) -> int:
        self.pointer += 1
        return self.arr[self.pointer - 1]

    def hasNext(self) -> bool:
        return self.pointer < len(self.arr)

# Create a stack and append the deepest left child node of current node to current node.
# [left deepest, left second deepest, ... , current node].
# Every time we perform a next operation, 
# we pop the last node in stack, 
# and do the above operation (append the left deepest child node) but do it for the right child node.

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        node = root
        while node:
            t = node
            node = node.left
            self.stack.append(t)

    def next(self) -> int:
        res = self.stack.pop()
        node = res.right
        while node:
            t = node
            node = node.left
            self.stack.append(t)
        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
