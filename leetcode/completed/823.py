from typing import List
from functools import cache

# We will sort the arr first.
# Iterate i from last to first,
# at every index i, we iterate check the numbers that are smaller than arr[i],
# and if arr[j]*x = arr[i] ===> x = arr[i] // arr[j] 
# exists in arr, we will add dfs(j)*dfs(arr[i] // arr[j]) to res.

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        indices = {arr[i]: i for i in range(len(arr))}
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i):
            res = 1
            for j in range(i-1, -1, -1):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in indices:
                    # print(arr[i], arr[j], arr[i]//arr[j])
                    res += dfs(j) * dfs(indices[arr[i] // arr[j]])
            return res % MOD
        
        res = 0
        for i in range(len(arr)-1, -1, -1):
            res += dfs(i)
        
        return res % MOD
    
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        indices = {arr[i]: i for i in range(len(arr))}
        MOD = 10 ** 9 + 7

        dp = [1] * len(arr)
        for i in range(len(arr)):
            for j in range(i-1, -1, -1):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in indices:
                    dp[i] += dp[j] * dp[indices[arr[i] // arr[j]]]
                    dp[i] %= MOD
        
        return sum(dp) % MOD