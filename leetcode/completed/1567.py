from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] <= 0:
            return 0

        res = 0

        start = 0
        first_negative = -1
        cur_is_negative = False

        for i, num in enumerate(nums):
            if num < 0:
                cur_is_negative = not cur_is_negative
                if first_negative == -1:
                    first_negative = i
            elif num == 0:
                first_negative = -1
                start = i + 1
                cur_is_negative = False
            else:
                if cur_is_negative:
                    res = max(res, i - first_negative)
                else:
                    res = max(res, i - start + 1)

        return res

        
        

sol = Solution()
print(sol.getMaxLen([5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
))