from typing import List

# Initialize one prefix and one suffix, 
# where prefix[i] denotes the shortest subarray which sum == target from 0 to i
# and   suffix[i] denotes the shortest subarray which sum == target from i to len(arr).
# Here we compute prefix and suffix using the 'leetcode 560 Subarray sum equal K technique' which runs in O(n) time.
# Lastly, we iterate from 0 to len(arr)-1 and keep 
# current_shortest = (left shortest subarray from 0 to i) + (right shortest subarray from i to len(arr) - 1) shortest.

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = []
        d = {0: -1}
        cur_sum = 0
        cur_min = float('inf')
        for i in range(n):
            cur_sum += arr[i]
            if cur_sum - target in d:
                cur_min = min(cur_min, i - d[cur_sum - target])
            d[cur_sum] = i
            prefix.append(cur_min)

        d = {0: n}
        suffix = []
        cur_sum = 0
        cur_min = float('inf')
        for i in range(n-1, -1 ,-1):
            cur_sum += arr[i]
            if cur_sum - target in d:
                cur_min = min(cur_min, d[cur_sum - target] - i)
            d[cur_sum] = i
            suffix.append(cur_min)
        suffix.reverse()

        res = float('inf')
        for i in range(n-1):
            res = min(res, prefix[i]+suffix[i+1])

        return res if res < float('inf') else -1