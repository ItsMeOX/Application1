from typing import List
from collections import defaultdict
from bisect import bisect_left

# Create a dictionary ('indices') which stores a list of indices of each number.
# It will look like this:      num: [idx1, idx2, idx3...]

# Consider we have array: [1,3,1,1,2,1,1,1]
# We take 1 as example here, 'indices' dictionary will be 1: [0,2,3,5,6,7]
# Here we take i = 2, which is 3 as example.
# the answer of i = 2 will be: 
# (3-0) + (3-2) + (5-3) + (6-3) + (7-3) = 3+1+2+3+4
#                                       = 13

# We can rewrite the summation as:
#    (3-0) + (3-2) + (5-3) + (6-3) + (7-3)
# =  3*2 - (0+2) + (5+6+7) - 3*3
# =  cur_idx*i - sum(from start to i-1) + sum(from i+1 to last) - cur_idx*(length-i-1)

# So, we can precompute sum(from start to i-1) and sum(from i+1 to last) by utilizing prefix and suffix sum.
# Then, we iterate through the 'nums' list again and apply the formula above and it will the result for each num in 'nums'.
# Also, when a number only occurs onces, we can just set the answer to be 0. (this is the case when len(indices[num]) == 1)


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        # find idx for each num
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)

        # compute prefix & suffix arr
        prefix = defaultdict(list)
        suffix = defaultdict(list)

        for key in indices.keys():
            n = len(indices[key])
            if n != 1:
                prefix[key] = [0] * (n+1)
                suffix[key] = [0] * (n+1)

                for i in range(1, n+1):
                    prefix[key][i] = prefix[key][i-1] + indices[key][i-1]
                
                for i in range(n-1, -1, -1):
                    suffix[key][i] = suffix[key][i+1] + indices[key][i]

        for i, num in enumerate(nums):
            if len(indices[num]) != 1:
                idx = bisect_left(indices[num], i)
                # prefix -> i
                # suffix -> i + 1
                res[i] = idx * i - prefix[num][idx] + suffix[num][idx+1] - (len(indices[num]) - idx - 1) * i

        return res
    
# We can further optimize the prefix and suffix sum.
# This can reduce the time complexity of O(nlogn) to O(n).
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        indices = defaultdict(list)

        for i, num in enumerate(nums):
            indices[num].append(i)

        for num, lis in indices.items():
            if len(lis) != 1:
                prefixSum = 0
                suffixSum = sum(lis)
                for i, cur_idx in enumerate(lis):
                    res[cur_idx] = i*cur_idx - prefixSum + suffixSum - cur_idx - (len(lis)-i-1)*cur_idx # here the formula is same but we have to subtract current num(index).
                    prefixSum += cur_idx
                    suffixSum -= cur_idx
        
        return res

