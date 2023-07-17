from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        dp = [[0,0] for _ in range(len(arr))] # longest inc, dec


        for i in range(1, len(arr)):
            # increasing
            if arr[i] > arr[i-1]:
                dp[i][0] = dp[i-1][0] + 1

            # decreasing
            if arr[i] < arr[i-1] and (dp[i-1][1] > 0 or dp[i-1][0] > 0):
                dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + 1

        res = 0
        for _, i in dp:
            res = max(res, i)


        return res+1 if res else 0
    


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_inc = max_dec = 0
        res = 0

        for i in range(1, len(arr)):

            # increasing
            if arr[i] > arr[i-1]:
                if max_dec:
                    max_dec = max_inc = 0
                max_inc += 1

            # decreasing
            elif arr[i] < arr[i-1] and max_inc > 0:
                if not max_dec:
                    max_dec = max_inc + 1
                else:
                    max_dec += 1
            
            # same altitude
            else:
                max_inc = max_dec = 0

            res = max(res, max_dec)

        return res+1 if res else 0

# 2 1 4 7 3 2 5
# 0 0 1 2 0 0 1
# 0 0 0 0 3 4 0


# 2 2 2
# 0 0 0
# 0 0 0

# 2 1 4 7 3 2 5
# 0 0 1 2 0 0 1
# 0 0 0 0 3 4 0


# 2 2 2
# 0 0 0
# 0 0 0