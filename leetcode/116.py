"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque
        depth = 1

        if not root:
            return

        q = deque([root])
        while q:
            node = q.popleft()
            for x in range(depth):
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if x == depth - 1:
                    node.next = None
                else:
                    node.next = q.popleft()
                    node = node.next
            depth *= 2

        return root
            