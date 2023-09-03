from typing import List
from bisect import bisect_left

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = -1
        maximum = -1
        mode = 0
        sums = 0
        total_count = sum(count)
        prefix = [0] * 257

        for i in range(256):
            if count[i]: 
                print(i)
                # min
                if minimum == -1:
                    minimum = i
                
                # max
                maximum = i
                
                # mean
                sums += ( i * count[i] )

                # mode
                if count[i] > count[mode]:
                    mode = i
            
            prefix[i+1] = count[i] + prefix[i]           

        median = bisect_left(prefix, total_count // 2 + 1) - 1
        if total_count % 2 == 0:
            median = (median + bisect_left(prefix, total_count // 2) - 1) / 2

        return [minimum, maximum, sums / total_count, median, mode]