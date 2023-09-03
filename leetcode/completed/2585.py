from typing import List

# MLE
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        types.append([-1, -1])
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(i, cur_remain, points):

            if i == len(types)-1:
                return points == target
            
            if points > target:
                return 0
            
            if cur_remain == 0:
                return dfs(i+1, types[i+1][0], points)
            
            # not take
            res = dfs(i+1, types[i+1][0], points)

            # take
            res += dfs(i, cur_remain-1, points + types[i][1])

            return res % MOD
        
        return dfs(0, types[0][0], 0) % MOD

# Instead of dfs(i, cur_question_count, points),
# we can reduce the states to only dfs(i, points).
# We do this by iterate j from 0 to count of current question.
# Here j means how many question we will take from the current question stack.
# Every time we took current question, we will continue to next stack.

from functools import lru_cache
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(i, points):

            if i == len(types)-1:
                return points == target
            
            if points > target:
                return 0
            
            res = 0
            for j in range(types[i][0]+1):
                res += dfs(i+1, points + types[i][1] * j)

            return res % MOD
        
        return dfs(0, 0)
    
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        dpb = [0] * (target+1)
        dpb[target] = 1

        for i in range(len(types)):
            dpf = [0] * (target+1)
            for point in range(target+1):
                for j in range(types[i][0]+1):
                    next_point = point + types[i][1] * j
                    if next_point > target: continue
                    dpf[point] += dpb[next_point] % MOD
            dpb = dpf
        
        return dpf[0] % MOD