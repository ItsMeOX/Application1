from typing import List

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        mapper = {} # map count of digit to maximum number
        res = -1

        for i in range(len(nums)):
            cur_count = sum([int(j) for j in str(nums[i])])
            if cur_count in mapper:
                res = max(res, nums[i] + mapper[cur_count])
                mapper[cur_count] = max(mapper[cur_count], nums[i])
            else:
                mapper[cur_count] = nums[i]

        return res
    
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mapper = {} # map count of digit to maximum number
        res = -1

        def getDigitSum(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        for i in range(len(nums)):
            cur_count = getDigitSum(nums[i])
            if cur_count in mapper:
                res = max(res, nums[i] + mapper[cur_count])
                mapper[cur_count] = max(mapper[cur_count], nums[i])
            else:
                mapper[cur_count] = nums[i]

        return res