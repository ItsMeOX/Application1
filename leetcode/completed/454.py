from typing import List

# Create a dictionary which 
# key is the sum of every pair of nums1 and nums2
# value is the number of appearance of sum.
# Then for every pair of nums3 and nums4, check if 0-(n3+n4) is in dictionary,
# if yes then res += dictionary[-(n3+n4)].

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        seen = {}
        res = 0
        for n1 in nums1:
            for n2 in nums2:
                seen[n1+n2] = seen.get(n1+n2, 0) + 1
    
        for n3 in nums3:
            for n4 in nums4:
                if -n3-n4 in seen:
                    res += seen[-n3-n4]
        
        return res