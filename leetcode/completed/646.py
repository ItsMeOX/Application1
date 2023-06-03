class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort()
        dp = [1] * len(pairs)
        res = 1

        for i in range(len(pairs)-2, -1, -1):
            temp = 0
            for j in range(i+1, len(pairs)):
                if pairs[j][0] > pairs[i][1]:
                    temp = max(temp, dp[j])

            dp[i] += temp

            res = max(res, dp[i])

        return res  

sol = Solution()
print(sol.findLongestChain([[1,2],[1,2]]))
# print(sol.findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]])) # 3