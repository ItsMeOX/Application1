from typing import List

# Here we will assign the most frequently requested index to the largest number in nums,
# secondly most frequently requested index to 2nd largest valued num...

# We can keep track of prefix sum of frequency in 'frequency' array.
# For every start, end in requests,
# we can frequency[start]++ and frequency[end+1]--,
# so that when we iterate i from 0 to len(frequency), the interval frequency[start ~ end] will all have 1,
# and frequency[end+1 ~ ...] will be frequency of 0 again.

# The idea is we will collect the starting and ending point of allrequests first,
# then iterate and culumate the frequency between each range at last together.

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()

        frequency = [0] * len(nums)
        for s, e in requests:
            frequency[s] += 1
            if e+1 < len(nums):
                frequency[e+1] -= 1
        
        for i in range(1, len(nums)):
            frequency[i] += frequency[i-1]
        frequency.sort()

        res = 0
        for i in range(len(nums)):
            res += (frequency[i] * nums[i])
            res %= MOD

        return res