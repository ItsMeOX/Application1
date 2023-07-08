from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[1,1] for _ in range(n)] # cnt if i+1 > i, cnt if i+1 < i
        res = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                dp[i][0] += dp[i-1][1]
                res = max(res, dp[i][0])
            elif arr[i] < arr[i-1]:
                dp[i][1] += dp[i-1][0]
                res = max(res, dp[i][1])

        return res

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        higher = 1
        lower = 1
        res = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                higher = lower + 1 # higher is dp[i][0], lower is dp[i-1][1]
                lower = 1
                res = max(res, higher)
            elif arr[i] < arr[i-1]:
                lower = higher + 1 # lower is dp[i][1], higher is dp[i-1][0]
                higher = 1
                res = max(res, lower)
            else:
                lower = higher = 1

        return res
        

        
