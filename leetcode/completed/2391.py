from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        record = {
            'M': [0, 0],
            'P': [0, 0],
            'G': [0, 0]
        }
        distance = 0

        for i in range(len(garbage)):
            if i > 0:
                distance += travel[i-1]
            for trash in garbage[i]:
                record[trash][0] += 1
                record[trash][1] = distance
        
        return sum(sum(val) for val in record.values())