from typing import List
from collections import defaultdict

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = defaultdict(list)
        for i in range(len(nums)):
            counter[nums[i]].append(i)

        dominant = max(counter.keys(), key=lambda e: len(counter.get(e)))

        for i in range(len(counter[dominant])):
            left_len = counter[dominant][i] + 1
            right_len = len(nums)-left_len
            left_count = i + 1
            right_count = len(counter[dominant]) - left_count
            if left_count * 2 > left_len and right_count * 2 > right_len:
                return counter[dominant][i]

        return -1
    
# Count the frequency of numbers in nums array and get the dominant number from counter dictionary.
# Iterate i from 0 to length of 'nums' array through the 'nums' array and check if nums[i] is the dominant number or not.
# If yes check if left count * 2 > left length and right count * > right length.
# If true then return the index.
# If there is no valid separation then return -1.

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counter = defaultdict(list)
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        dominant = max(counter.keys(), key=lambda e: counter.get(e))
        left_count = 0

        for i in range(n):
            if nums[i] == dominant:
                left_len = i + 1
                right_len = n - left_len
                left_count += 1
                right_count = counter[dominant] - left_count
                if left_count * 2 > left_len and right_count * 2 > right_len:
                    return i

        return -1