from typing import List

# Take the left and right largest height for every index.
# The amount of water at index i = min(left highest, right highest) - height[i].

class Solution:
    def trap(self, height: List[int]) -> int:

        next_greater = [0] * len(height)
        prev_greater = [0] * len(height)

        tallest = height[0]
        for i in range(1, len(height)):
            tallest = max(tallest, height[i])
            prev_greater[i] = tallest

        tallest = height[-1]
        for i in range(len(height)-2, -1, -1):
            tallest = max(tallest, height[i])
            next_greater[i] = tallest

        res = 0
        for i in range(1, len(height)-1):
            res += min(next_greater[i], prev_greater[i]) - height[i]                

        return res