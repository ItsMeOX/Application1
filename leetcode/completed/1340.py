from typing import List

# Greedy will not work here obviously, so we can have use DP.
# For every index of arr, if check from i to i-d,
# 1. if arr[i-d] is higher than arr[d] or i is out of bound, break. (same for right arr[i+d])
# 2. else continue dfs at i and add 1 as we made a jump.
# We have to add 1 for final ans as we have made n jump and we want n+1 pillars.

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        memo = [-1] * len(arr)

        def dfs(i):
            if memo[i] != -1:
                return memo[i]
            # left
            res = 0
            for j in range(1, d+1):
                if i-j >= 0 and arr[i-j] < arr[i]:
                    res = max(res, dfs(i-j) + 1)
                else:
                    break

            # right
            for j in range(1, d+1):
                if i+j < len(arr) and arr[i+j] < arr[i]:
                    res = max(res, dfs(i+j) + 1)
                else:
                    break
                    
            memo[i] = res

            return res
        
        res = 0
        for i in range(len(arr)):
            res = max(res, dfs(i))

        return res + 1
    
# Can be optimized to O(N).