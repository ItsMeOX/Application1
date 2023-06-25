# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root= Optional[TreeNode], k= int) -> int:
        q = deque()
        q.append(root)

        sums = []
        print(root.left)
        while q:
            cur_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            print()
            sums.append(cur_sum)

        print(sums)

        if k >= len(sums):
            return -1

        return sorted(sums)[-k]
    
sol = Solution()