class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1,len(nums)):
            print(i)
            nums[i] += nums[i-1]
        
        print(nums)
sol = Solution()
sol.runningSum([0,1,2,3,4,5])


print(3%5)