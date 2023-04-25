class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        det = 0
        for num in nums:
            det ^= num
            print(det)
        return det
    

sol = Solution()    
print(sol.singleNumber([2,3,2,3,1]))