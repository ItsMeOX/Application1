class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        nums_len = len(nums)
        dp = [{} for _ in range(nums_len)]
        res = 1
        for i in range(nums_len-2, -1, -1):
            for j in range(i+1, nums_len):
                if nums[j] - nums[i] in dp[i]:
                    dp[i][nums[j]-nums[i]] = max(dp[i][nums[j] - nums[i]], dp[j].get(nums[j]-nums[i], 0) + 1)
                else:
                    dp[i][nums[j]-nums[i]] = dp[j].get(nums[j]-nums[i], 0) + 1
        
        for i in range(nums_len-1):
            res = max(res, max(dp[i].values()))
        return res + 1
        

sol = Solution()
print(sol.longestArithSeqLength([44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]
))