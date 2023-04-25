class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if n in self.memo:
            return self.memo[n]

        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = res

        return self.memo[n]