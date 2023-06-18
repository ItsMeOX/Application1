class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_j = []
        res = 0
        for n in range(1, len(values)):
            max_j.append(values[n]-n)
        for n in range(len(max_j)-2, -1, -1):
            max_j[n] = max(max_j[n+1], max_j[n])
        for i in range(len(values)-1):
            res = max(res, i+values[i]+max_j[i])
        return res

class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_i = 0
        res = 0
        for i in range(1, len(values)):
            max_i = max(max_i, values[i-1]+i-1)
            res = max(res, max_i+values[i]-i)
        return res

sol = Solution()
print(sol.maxScoreSightseeingPair([1,2]))