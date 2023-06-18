class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx, val = stack.pop()
                res[idx] = i - idx
            stack.append((i, t))

        return res
from random import randint
sol = Solution()
print(sol.dailyTemperatures([randint(30, 100) for _ in range(10 ** 5)]))