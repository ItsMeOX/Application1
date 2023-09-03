from typing import List

# Base cases:
# If i == n, we have rolled n times, so return 0.

# Cases:
# For each index i (rolled how many times), 
# and for each number in 1 to 6,
# we will roll rollMax[number] times, 
# so i += rolls.

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        def dfs(i, prev):

            if i == n:
                return 1
            
            res = 0
            for num in range(6):
                if num == prev: continue
                for roll in range(1, rollMax[num]+1):
                    if i+roll > n: break
                    res += dfs(i+roll, num)
            
            return res
        
        return dfs(0, -1)
    
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7

        dp = [[0]*7 for _ in range(n)]
        dp.append([1]*7)

        for i in range(n-1, -1, -1):
            for prev in range(7):
                for num in range(6):
                    if num == prev: continue
                    for roll in range(1, rollMax[num]+1):
                        if i+roll > n: break
                        dp[i][prev] += dp[i+roll][num]
                        dp[i][prev] %= MOD

        return dp[0][-1] % MOD