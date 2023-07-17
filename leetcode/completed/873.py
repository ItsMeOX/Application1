from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        memo = set(arr)

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                prev, cur = arr[i], arr[j]
                cur_longest = 2
                while prev + cur in memo:
                    temp = prev + cur
                    prev = cur
                    cur = temp
                    cur_longest += 1

                if cur_longest >= 3:
                    res = max(res, cur_longest)

        return res