from typing import List
from collections import defaultdict

# Check gradients after each points instead of 
# checking gradients after all points, 
# to prevent 
# 1. floating point precision error
# 2. same gradient but different line.

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1
        res = 0
        n = len(points)

        for i in range(n):
            gradients = defaultdict(int)
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                g = (y1-y2) / (x1-x2) if x1-x2 != 0 else float('inf')
                gradients[g] += 1
            res = max(res, max(gradients.values() if gradients else [0]))

        return res + 1
    

# Floating point precision error (y_intercept)
# why ??
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1

        gradients = defaultdict(set)
        n = len(points)

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                g = (y1-y2) / (x1-x2) if x1-x2 != 0 else float('inf')
                y_intercept1 = y1-g*x1 if g != float('inf') else x1
                y_intercept2 = y2-g*x2 if g != float('inf') else x2
                gradients[(y_intercept1, g)].add((x1, y1))
                gradients[(y_intercept2, g)].add((x2, y2))
        
        print(gradients)

        return len(max(gradients.values(), key = len))