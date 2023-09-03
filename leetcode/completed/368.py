from typing import List

# Keep two arrays, one for tracking the largest divisible subset length, another one for tracking previous divisible num index.
# Sort the array first, so that we can guarantee nums[j] < nums[i].
# Iterate through the nums and if nums[i] % nums[j] == 0 and longest[j]+1 is longest subset length, 
# then we will update longest[i] to longest[j]+1 and prev[i] to j.
# After populating the prev and longest array, we start from the largest index and append nums[max_index] to res, and traverse max_index to prev[max_index].

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        longest = [1] * len(nums)
        prev = [i for i in range(len(nums))]
        max_index = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and longest[j]+1 > longest[i]:
                    longest[i] = longest[j] + 1
                    prev[i] = j
            if longest[max_index] < longest[i]:
                max_index = i

        res = [nums[max_index]]
        while prev[max_index] != max_index:
            max_index = prev[max_index]
            res.append(nums[max_index])

        return res