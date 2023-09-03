from typing import List

# Create prefix and suffix array which array[i] stores the longest
# decreasing length from front/back to back/front.
# If prefix[i] and suffix[i] >= time then add i to res.

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        prefix = [0]*(n+1)
        suffix = [0]*(n+1) # Can variable instead of a whole list here.

        for i in range(1, n):
            if security[i] <= security[i-1]:
                prefix[i] = prefix[i-1] + 1

        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                suffix[i] = suffix[i+1] + 1

        res = []

        for i in range(time, len(security)-time):
            if prefix[i] >= time and suffix[i] >= time:
                res.append(i)
        
        return res
    
# Using set instead of prefix array.

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        res = []
        left = set()
        
        cnt = 0
        for i in range(n):
            if i > 0 and security[i] <= security[i-1]:
                cnt += 1
            else:
                cnt = 0
            if cnt >= time:
                left.add(i)

        cnt = 0
        for i in range(n-1, -1, -1):
            if i+1 < n and security[i] <= security[i+1]:
                cnt += 1
            else:
                cnt = 0
            if cnt >= time and i in left:
                res.append(i)
        
        return res