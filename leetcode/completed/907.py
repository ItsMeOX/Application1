class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int: #O(n)
        res = 0
        MOD = 10 ** 9 + 7
        count = [[0,0] for _ in range(len(arr))]  # [left, right]
        stack = []

        for i in range(len(arr)):
            while (stack and arr[stack[-1]] > arr[i]):
                idx = stack.pop()
                count[idx][1] = i - idx - 1
            stack.append(i)

        while stack:
            idx = stack.pop()
            count[idx][1] = len(arr) - idx - 1

        for i in range(len(arr)-1, -1, -1):
            while (stack and arr[stack[-1]] >= arr[i]):
                idx = stack.pop()
                count[idx][0] = idx - i - 1
            stack.append(i)

        while stack:
            idx = stack.pop()
            count[idx][0] = idx

        for i, (left, right) in enumerate(count):
            res += (left * (right + 1) + right + 1) * arr[i]

        return res % MOD
            
sol = Solution()
print(sol.sumSubarrayMins([71,55,82,55]
))
