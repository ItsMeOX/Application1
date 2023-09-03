from heapq import heappop, heappush
from typing import List

# Initialize a heap which stores (current cost, current x, current y).
# Initialize a set 'visited'.
# We will explore the current lowest cost path each iteration, 
# if we are at lowest cost path and we visited (x, y), then we will add (x, y) to 'visited' as the next time we visited (x, y),
# it will need more cost.
# At current (x, y), we will append path from (x, y) to (target_x, target_y),
#                    we will also append path from (x, y) to each (new_x, new_y) of specialRoads.
# Each append, we will calculate the cost and append it along with new_x, new_y to 'heap'.
# The first time we reach (target_x, target_y), that will be our lowest cost possible to travel from (start_x, start_y) to (target_x, target_y).

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        heap = [] # cost, x, y
        heap.append((0, start[0], start[1]))
        visited = set()

        while heap:
            cur_cost, x, y = heappop(heap)
            if x == target[0] and y == target[1]:
                return cur_cost
            if (x, y) in visited:
                continue
            visited.add((x, y))

            heappush(heap, (cur_cost + abs(target[0]-x)+abs(target[1]-y), target[0], target[1]))

            for x1, y1, x2, y2, cost in specialRoads:
                heappush(heap, (cur_cost + abs(x-x1) + abs(y-y1) + cost, x2, y2))