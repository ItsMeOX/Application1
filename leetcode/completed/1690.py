from typing import List
from functools import lru_cache

# Bob -> try to minimize score.
# Alice -> try to maximize score.
# Just need to make sure that they obtain maximum score so that their score difference can be minimized.
# Score = sum(left to right) - maximized opponent score.
# The sum from left to right can be calculated in O(1) time by using a prefix sum.

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pref = [0] * (len(stones)+1)
        for i in range(1, len(stones)+1):
            pref[i] = pref[i-1] + stones[i-1]

        @lru_cache(2000)
        def minimax(left, right):
            if left == right:
                return 0
            
            res = max(
                pref[right-1] - pref[left] - minimax(left, right-1),
                pref[right] - pref[left+1] - minimax(left+1, right)
            )

            return res

        return minimax(0, len(stones))
    
sol = Solution()
print(sol.stoneGameVII([481,905,202,250,371,628,92,604,836,338,676,734]))