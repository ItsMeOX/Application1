from typing import List
from bisect import bisect_right

# We need the number of ages between (0.5*ages[x]+7, x]

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        res = 0

        for age in ages:
            res += max(0, bisect_right(ages, age) - 1 - bisect_right(ages, age // 2 + 7))

        return res

from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        prefix = [0] * 121
        res = 0

        for i in range(1, 121):
            prefix[i] += prefix[i-1] + counter[i]

        for age in ages:
            age2 = age // 2 + 7
            if age2 < age:
                res += prefix[age] - prefix[age2] - 1

        return res