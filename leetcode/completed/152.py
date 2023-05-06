class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        currMin , currMax = 1 , 1
        res = nums[0]

        for num in nums:
            temp = (num, num*currMax, num*currMin)
            currMax , currMin = max(temp) , min(temp)
            if res < currMax:
                res = currMax

        return res

        # B = nums[::-1]
        # for i in range(1,len(nums)):
        #     nums[i] *= nums[i-1] or 1
        #     B[i] *= B[i-1] or 1
        
        # return max(nums+B)

nums = [1,4,-4,5,-2,-1,-1,-2,3]


sol = Solution()
print(sol.maxProduct(nums))