from typing import List
from collections import deque

# Create a dictionary that maps source num -> destination num.
# Initialize cur (current number) = 0, 
# We walk from bottom left corner to top left corner in Boustrophedon style and increase cur by 1 every step we move.
# Every time we reach a cell where its value is not -1, we add 'cur' as key and value of current board cell as value to dictionary.
# We then perform BFS and find the shortest path available.

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        portal = {}
        direction = 1
        cur = 1

        for row in board[::-1]:
            for col in row[::direction]:
                if col > -1:
                    portal[cur] = col
                cur += 1
            direction = -direction
        
        q = deque()
        q.append(1)
        visited = set()
        visited.add(1)
        res = 0
        while q:
            for _ in range(len(q)):
                pos = q.popleft()
                if pos == n ** 2:
                    return res
                
                for i in range(1, 7):
                    # -------------------
                    # do not check if pos + i is visited here, 
                    # -------------------
                    # because if we teleported to a cell that is also a portal,
                    # and we marked it as visited, but we have not actually visited the destination in the portal.
                    # if portal: check dest in portal is visited or not,
                    # if not portal: check if cell is visited or not.
                    if pos + i in portal:
                        if portal[pos + i] not in visited:
                            visited.add(portal[pos+i])
                            q.append(portal[pos + i])
                    else:
                        if pos + i not in visited:
                            visited.add(pos + i)
                            q.append(pos + i)
                
            res += 1

        return -1