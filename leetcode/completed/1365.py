from typing import List

# Use counting sort and prefix sum to calculate the number of num < nums[i].
# The number of num < nums[i] = prefix[nums[i]-1].

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        counter = [0] * (max(nums)+1)

        for num in nums:
            counter[num] += 1
        
        counter2 = counter[:]

        for i in range(1, len(counter)):
            counter[i] += counter[i-1]
        
        res = []
        for num in nums:
            res.append(counter[num] - counter2[num])
        
        return res
    
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        counter = [0] * (max(nums)+1)

        for num in nums:
            counter[num] += 1
        
        for i in range(1, len(counter)):
            counter[i] += counter[i-1]
        
        res = []
        for num in nums:
            res.append(counter[num - 1] if num != 0 else 0)
        
        return res