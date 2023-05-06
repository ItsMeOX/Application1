class Solution:
    def maxSubArray(self, nums: list[int]) -> int: # Kadane's Algorithm
                

        max_sum = -float('inf')
        cumulative = 0

        for i in nums:
            cumulative += i
            if max_sum < cumulative:
                max_sum = cumulative

            if cumulative < 0:
                cumulative = 0  # if sub array before current index < 0, discard the sub array and recalculate cumulative at current idx
            
        return max_sum



                
                
arr = [2,-1,3,-1]


sol = Solution()
print(sol.maxSubArray(arr))