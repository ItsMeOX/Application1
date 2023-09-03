from typing import List

# Check for the four areas,
# 1. if all the elmns inside are the same, set val to the only elm, set isLeaf to 1, and return node.
# 2. else, divide the area into four equal sized rectangular areas again.

# TC: O(N^2 * logN), can be reduced to O(N^2)
# SC: O(N^2)

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(x1, x2, y1, y2):
            val = grid[y1][x1]
            isLeaf = True

            node = Node(val, isLeaf, None, None, None, None)

            for x in range(x1, x2):
                for y in range(y1, y2):
                    if grid[y][x] != val:
                        isLeaf = False
                        break
                if not isLeaf: break

            if not isLeaf:
                node.isLeaf = False
                node.topLeft     = dfs(x1          , (x1+x2) // 2 , y1           , (y1+y2) // 2)
                node.topRight    = dfs((x1+x2) // 2, x2           , y1           , (y1+y2) // 2)
                node.bottomLeft  = dfs(x1          , (x1+x2) // 2 , (y1+y2) // 2 , y2          )
                node.bottomRight = dfs((x1+x2) // 2, x2           , (y1+y2) // 2 , y2          ) 

            return node

        return dfs(0, n, 0, n)