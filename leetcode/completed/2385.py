from typing import Optional
from collections import defaultdict, deque

# Convert tree to graph and perform normal BFS to find the maximum distance from start to other nodes.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjList = defaultdict(list)
        q = [root]

        while q:
            node = q.pop()
            if node.left:
                adjList[node.val].append(node.left.val)
                adjList[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                adjList[node.val].append(node.right.val)
                adjList[node.right.val].append(node.val)
                q.append(node.right)

        q = deque([start])
        visited = set([start])
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adjList[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            res += 1

        return res - 1