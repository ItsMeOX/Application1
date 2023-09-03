from functools import cache

# minimax algorithm

class Solution:
    def canWinNim(self, n: int) -> bool:

        @cache
        def dfs(n):
            if n <= 3:
                return 1

            return max(-dfs(n-1), -dfs(n-2), -dfs(n-3))

        return dfs(n) == 1
    
can_win = 0
sol = Solution()
for i in range(100):
    if sol.canWinNim(i):
        print(i)
        can_win += 1
print(can_win)

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4