from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        pos = {}
        res = 0

        for i, color in enumerate(colors):
            if color not in pos:
                pos[color] = i
            for key in pos.keys():
                if key != color:
                    res = max(res, i - pos[key])
                    
        return res

# Consider the following example:
# 1 2 1 1 1
# The maximum distance will be (idx of last color) - (smallest idx of color that is different to last color)
# In this case will be 4 - 2 = 2
# If the case is:
# 1 1 1 2 1
# it means that we have to check from last to first and get the maximum from right to left also.

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_l_distance = max_r_distance = 0

        for i in range(len(colors)):
            if colors[i] != colors[-1]:
                max_l_distance = len(colors)-i-1
                break

        for i in range(len(colors)-1, -1, -1):
            if colors[i] != colors[0]:
                max_r_distance = i
                break

        return max(max_l_distance, max_r_distance)