class Solution:
    def numSquares(self, n: int) -> int:
        sqr_nums = []
        num = 1
        while num**2 <= n:
            sqr_nums.append(num**2)
            num += 1

        dp = [n+1] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for sqr_num in sqr_nums:
                if i >= sqr_num:
                    dp[i] = min(dp[i], 1 + dp[i - sqr_num])

        return (dp[-1] if dp[-1] != n+1 else -1)


sol = Solution()
print(sol.numSquares(100001))