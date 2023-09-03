from typing import List

# Calculate the frequency of number for each odd and even index of 'nums' array.
# Then sort the odds and even keys by their values.

# Case 1:
# If the number of maximum frequency of even and odd index are different, then change all the
# numbers in 'nums' to maximum frequency of number each.
# Ex: [3,1,3,2,3,2] -> [3,2,3,2,3,2]
# The number of num needed to be changed will be len(nums) - max(odds) - max(evens)

# Case 2:
# If the number of maximum frequency of even and odd index are same, then we need to try 
# second frequent numbers for either odd or even and return the minimum.
# Ex:     [4,2,1,4,4,4,1,3,4,1,1,4,4]
# odd     [4,2,4,4,4,4,4,3,4,1,4,4,4] -> 3
#         [4,2,4,2,4,2,4,2,4,2,4,2,4] -> 5   -> 3+5 = 8
# even    [4,4,1,4,4,4,1,4,4,4,1,4,4] -> 3  
#         [1,4,1,4,1,4,1,4,1,4,1,4,1] -> 4   -> 3+4 = 7

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odds = {0:0}
        even = {0:0}

        for i in range(len(nums)):
            if i & 1:
                odds[nums[i]] = odds.get(nums[i], 0) + 1
            else:
                even[nums[i]] = even.get(nums[i], 0) + 1

        odd_keys = sorted(odds.keys(), key = lambda e: odds[e])
        even_keys = sorted(even.keys(), key = lambda e: even[e])

        if odd_keys[-1] != even_keys[-1]:
            return len(nums) - odds[odd_keys[-1]] - even[even_keys[-1]]

        res1 = len(nums) - odds[odd_keys[-1]] - even[even_keys[-2]]
        res2 = len(nums) - even[even_keys[-1]] - odds[odd_keys[-2]]

        return min(res1, res2)

# [4,2,1,4,4,4,1,3,4,1,1,4,4]