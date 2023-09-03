from typing import List
from collections import defaultdict
from functools import lru_cache

# We initalize a dictionary 'layers' which stores the chairs available each row(layer). Format: row: [...indices of chairs].
# Then we perform a dfs, starting from row = 0.
# For each chair in each row, we either take or not take the chair.

# Here, c is index of current layers[r].
# If c reaches the end of layers[r], then we start dfs at new row. So row+1, c=0, prevMask=currMask, currMask=0.
# 1. If we not take, then skip to c + 1.
# 2. If we take, we have to decide whether we can take current chair.
#    We do this by comparing last bitmask and current bitmask, where bitmask[i] represents that we have taken the chair or not. 1 if yes, 0 if no.
#    For example:
#    prevMask = 01000
#    currMask = 00000
#    At i = 2, we check that neighbour chair is occupied or not by checking either currMask[i-1], currMask[i+1] is 1 or not. If either is 1 then it is not valid.
#              we check that top left and top right chair is occupied or not by checking either prevMask[i-1], prevMask[i+1] is 1 or not.
#              In this case because that prevMask[i-1] is 1, so i = 2 is not valid.
#    At i = 3, it is valid, so we can take this chair by setting currMask[i] to 1, then continue dfs at c + 1, also add 1 to res.

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        layers = defaultdict(list)

        for r in range(m-1, -1, -1):
            for c in range(n):
                if seats[r][c] == '.':
                    layers[r].append(c)
        
        def valid(c, prevMask, currMask):
            if ((1 << c+1) & currMask) or ((1 << c+1) & prevMask): # cannot do (1<<(c+1)) & currMask & prevMask.
                return False
            if c-1 >=0 and ((1 << c-1) & currMask or ((1 << c-1) & prevMask)): # if c == 0, no need to check left side, also cannot << -1.
                return False
            return True

        @lru_cache(None)
        def dfs(r, c, prevMask, currMask): # r = row of seats, c = index of layers[r]
            if r == m:
                return 0
            if c == len(layers[r]):
                return dfs(r+1, 0, currMask, 0)
            
            # not take
            res = dfs(r, c+1, prevMask, currMask)

            # take
            if valid(layers[r][c], prevMask, currMask):
                currMask |= (1 << layers[r][c])
                res = max(res, 1 + dfs(r, c+1, prevMask, currMask))

            return res
        
        return dfs(0, 0, 0, 0)


# My initial approach (Memory limit exceeded even with bitmask as it requires at most 2^64 for bitmasking):

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        chairs = []
        directions = ((0, -1), (0, 1), (1, -1), (1, 1)) # left, right, bottom left, bottom right

        for r in range(m-1, -1, -1):
            for c in range(n):
                if seats[r][c] == '.':
                    chairs.append((r, c))

        def valid(r, c, visited):
            for dr, dc in directions:
                if (r+dr, c+dc) in visited:
                    return False
            return True

        def dfs(i, visited):
            if i == len(chairs):
                return 0
            
            r, c = chairs[i]
            # skip
            res = dfs(i+1, visited)

            # take
            if valid(r, c, visited):
                visited.add((r, c))
                res = max(res, 1 + dfs(i+1, visited))
                visited.remove((r, c))

            return res
        
        return dfs(0, set())