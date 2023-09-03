from collections import deque
from typing import List

# Using monotonic queue here.
# Iterate through the x,y points, 
# We want to maximize y1 + y2 + |x1 - x2| , where x1,y1 are old points and x2,y2 are current points.
# y1 + y2 + |x1 - x2| 
# = x2 - x1 + y1 + y2 
# = (y1 - x1) + x2 + y2.
# Every iteration, we will append (x2, y2-x2) to q.
# After first iteration, we want to maximize y1 - x1, if y1 - x1 < y2 - x2, we can discard the last point, which is (x1, y1-x1).
# If x1 < x2 - k, we can also discard the point.
# Before adding current point to q, we will compare res with x2 + y2 + q[0][1](which is (y1-x1)) and update res with the larger value.

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque() # (x, max_y)
        res = -float('inf')

        for x, y in points:
            while q and q[0][0] < x - k:
                q.popleft()

            if q:
                res = max(res, x+y+q[0][1]) # x2 - x1 + y1 + y2
            
            while q and q[-1][1] <= y-x:
                q.pop()

            q.append((x, y-x))

        return res
    
sol = Solution()
print(sol.findMaxValueOfEquation(points = [[-12,-5],[-9,-6],[-8,-2],[-7,-20],[-6,-15],[-4,-20],[5,3],[14,-6],[19,19]], k = 9))