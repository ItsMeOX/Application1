from typing import List


# Here because we are XORing all the num in nums,
# for each binary digit, we want only one '1', and the rest are '0' so that we can get the maximum final XOR.
# Because that nums[i] AND (nums[i] XOR x), we can always choose a x such that
# any amount of binary digit of nums[i] can change from '1' to '0',
# and note that we cannot change from '0' to '1' because of AND.
# Instead of find which which binary digit has '1' which has not,
# we can just OR all the numbers in nums, because if there is atleast one '1',
# then we can always make it '1' after XORing all the numbers in nums.

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res |= num            

        return res