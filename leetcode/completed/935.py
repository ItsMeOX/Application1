import sys
sys.setrecursionlimit(10000000)


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        memo = {}

        next_steps = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [3,9,0],
            5: [],
            6: [1,7,0],
            7: [2,6],
            8: [1,3],
            9: [2,4]
        }


        def dfs(num, step):
            if step == n:
                return 1

            if (num, step) in memo:
                return memo[(num, step)]

            res = 0
            for next_step in next_steps[num]:
                res += dfs(next_step, step+1)

            res %= MOD
            memo[(num, step)] = res

            return res

        res = 0
        for i in range(10):
            res += dfs(i, 1)
            res %= MOD

        return res

class Solution:
    def knightDialer(self, n: int) -> int: # bottom up
        MOD = 10 ** 9 + 7
        next_steps = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [3,9,0],
            5: [],
            6: [1,7,0],
            7: [2,6],
            8: [1,3],
            9: [2,4]
        }

        steps = [[0] * 10 for _ in range(n)]
        for i in range(10):
            steps[0][i] = 1

        for step in range(1, n):
            for num in range(10):
                for next_step in next_steps[num]:
                    steps[step][num] += steps[step-1][next_step]

        return sum(steps[-1]) % MOD
    
class Solution:
    def knightDialer(self, n: int) -> int: # bottom up with memory optimization
        MOD = 10 ** 9 + 7
        next_steps = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [3,9,0],
            5: [],
            6: [1,7,0],
            7: [2,6],
            8: [1,3],
            9: [2,4]
        }

        steps_back = [1] * 10

        for step in range(1, n):
            steps_front = [0] * 10
            for num in range(10):
                for next_step in next_steps[num]:
                    steps_front[num] += steps_back[next_step]
            steps_front[num] %= MOD
            steps_back = steps_front


        return sum(steps_back) % MOD

sol = Solution()
print(sol.knightDialer(1000))