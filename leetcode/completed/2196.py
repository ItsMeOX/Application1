# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
from collections import defaultdict
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # {node: [left_child, right_child]}
        adjList = defaultdict(list)

        # find root node (slow? more memory?)
        child_nodes = set(node[1] for node in descriptions)

        parent_val = 0
        for node in descriptions:
            if node[0] not in child_nodes:
                parent_val = node[0]
            if node[0] not in adjList:
                adjList[node[0]] = [-1, -1]
            adjList[node[0]][0 if node[2] else 1] = node[1]

        root = TreeNode(parent_val)
        def dfs(node):
            if node.val in adjList and adjList[node.val][0] != -1:
                node.left = TreeNode(adjList[node.val][0])
                dfs(node.left)
            if node.val in adjList and adjList[node.val][1] != -1:
                node.right = TreeNode(adjList[node.val][1])
                dfs(node.right)

        dfs(root)

        return root