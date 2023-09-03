from typing import List

# First initialize a dictionary which key is stones[i] and value is i,
# because we want to know if k+dk exists in stones array or not,
# (if it exists then we can jump otherwise no).
# Starting from index = 1, we can choose to jump k-1, k, k+1,
# we check if i+k+dk is in dictionary or not, if true the travel.

# Bases cases:
# If we reach len(stones)-1 then we can reach the last stone, return true.
# If we skip ahead of len(stones), then return false.

from functools import lru_cache
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1: return False

        stone_index = {stone:i for i, stone in enumerate(stones)}

        @lru_cache(None)
        def dfs(i, k): # k = step
            if i == len(stones)-1:
                return True
            
            if i >= len(stones):
                return False

            for dk in range(-1, 2):
                if k+dk <= 0: continue
                new_index = stones[i] + k + dk
                if new_index in stone_index and dfs(stone_index[new_index], k+dk):
                    return True
            
            return False
        
        return dfs(1, 1)
    

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1: return False
        if len(stones) <= 2: return True

        q = [(1, 1)] # stack not q
        seen = set((1, 1))
        stones_set = set(stones)

        while q:
            stone, k = q.pop()

            for dk in range(-1, 2):
                if k+dk <= 0: continue
                new_stone = stone+k+dk
                if new_stone in stones_set and (new_stone, k+dk) not in seen:
                    if new_stone == stones[-1]:
                        return True
                    q.append((new_stone, k+dk))
                    seen.add((new_stone, k+dk))

        return False