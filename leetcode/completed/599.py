from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        memo = {}
        least_sum = float('inf')

        for i in range(len(list1)):
            memo[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in memo and i + memo[list2[i]] <= least_sum:
                if i + memo[list2[i]] < least_sum:
                    res.clear()
                    least_sum = i + memo[list2[i]]
                res.append(list2[i])

        return res