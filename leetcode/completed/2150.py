from typing import List

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        res = []

        for key in counter:
            if counter[key] == 1 and key + 1 not in counter and key - 1 not in counter:
                res.append(key)

        return res
    
# can be done in O(nlogn) time and O(1) (except res list) space.