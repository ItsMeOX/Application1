from typing import List
from bisect import bisect_right

# Use binary search method to find LIS for each obstacles.
# the index (i for 0 ~ len(LIS)) found by binary search will be the length of LIS which obstacles[current] <= LIS[i].

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        lis = []
        res = [0] * len(obstacles)

        for i in range(len(obstacles)):
            obs = obstacles[i]
            j = bisect_right(lis, obs)
            if j == len(lis):
                lis.append(obs)
            else:
                lis[j] = obs
            
            res[i] = j + 1

        return res