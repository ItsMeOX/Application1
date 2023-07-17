from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = {}
        min_val = float('inf')
        res = 0

        for num in nums:
            record[num] = 1
            min_val = min(min_val, num)

        for key in list(record.keys()):
            if key in record:
                temp = 0
                while key-1 in record:
                    key -= 1
                
                while key in record:
                    del record[key]
                    temp += 1
                    key += 1
                res = max(res, temp)    
                
        return res
    
# as duplicated number does not contribute to answer here, we use set to remove duplicated number
# notice that at every starting point of subsequence, num - 1 will not exist in set
# for example, [1,2,3,6,7], 
# at starting point 1 and 6, 0 and 5 will not exist in set
# so we can iterate through the set and if num - 1 is not in set, we know it is one of the starting point and increase current num until the 
# number is not more in set and the length will be one of our answers, and the longest one is the final answer
# (here set is also good because of O(1) search time complexity)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                extend = 0
                while num + extend in nums_set:
                    extend += 1
                res = max(res, extend)

        return res