from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        sorted_arr = []

        def searchLarger(arr, num):
            lo, hi = 0, len(sorted_arr)-1
            while lo < hi:
                m = (lo+hi) // 2
                if arr[m] < num:
                    lo = m + 1
                else:
                    hi = m
            return lo

        def searchSmaller(arr, num):
            lo, hi = 0, len(sorted_arr)-1
            while lo <= hi:
                m = (lo+hi) // 2
                if arr[m] <= num:
                    lo = m + 1
                else:
                    hi = m - 1
            return lo - 1

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            sorted_arr.append(node.val)
            dfs(node.right)
        dfs(root)

        res = []
        for q in queries:
            min_idx = searchSmaller(sorted_arr, q)
            max_idx = searchLarger(sorted_arr, q)

            if min_idx == len(sorted_arr) or sorted_arr[min_idx] > q: min_idx = -1
            if sorted_arr[max_idx] < q: max_idx = -1

            min_val = sorted_arr[min_idx] if min_idx != -1 else -1
            max_val = sorted_arr[max_idx] if max_idx != -1 else -1

            res.append([min_val, max_val])

        return res

from bisect import bisect_left
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        sorted_arr = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            sorted_arr.append(node.val)
            dfs(node.right)
        dfs(root)

        res = []
        n = len(sorted_arr)
        for q in queries:
            i = bisect_left(sorted_arr, q)
            if i < n and sorted_arr[i] == q: res.append([sorted_arr[i], sorted_arr[i]])
            else:
                if i == 0:
                    res.append([-1, sorted_arr[i]])
                elif i == n:
                    res.append([sorted_arr[i-1], -1])
                else:
                    res.append([sorted_arr[i-1], sorted_arr[i]])

        return res
