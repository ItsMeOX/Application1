from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)):
            temp = 1
            for j in range(i+1, len(nums)):
                if nums[i] & nums[j] == 0:
                    nums[i] |= nums[j] # bitwise AND of every pair has to be 0
                    temp += 1
                else:
                    break

            res = max(res, temp)

        return res