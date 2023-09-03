from typing import List

# key = lambda e:(nums.count(e), -e) will not work duno why.

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        res = []

        for num in sorted(counter, key = lambda key: (counter[key], -key)):
            res += [num] * counter[num]
        
        return res