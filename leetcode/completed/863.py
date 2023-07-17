from collections import deque, defaultdict
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]: # set up adj list and BFS
        adjList = defaultdict(list) # can actually dict to store only parent instead of adj list

        q = deque()
        q.append(root)

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

        visited = set()
        q.append(target.val)
        visited.add(target.val)

        while k:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adjList[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            k -= 1

        return list(q)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]: # DFS set parent + BFS
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)
        
        q = deque()
        q.append(target)
        visited = set()
        visited.add(target)

        while k:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in [node.left, node.right, node.parent]:
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            k -= 1

        res = []
        for node in q:
            res.append(node.val)

        return res