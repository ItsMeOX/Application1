class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = len(nums)
        while(i < l):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                if i > 0:
                    i -= 1
                l -= 1
            else:
                i += 1

sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums)
print(nums)