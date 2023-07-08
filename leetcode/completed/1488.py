from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]: #O(n^2)
        res = [-1] * len(rains)
        rain_record = {}
        dry_day = []

        for i in range(len(rains)):
            if rains[i] > 0:
                if rains[i] in rain_record:
                    if not dry_day:
                        return []
                    else:
                        for day in dry_day:
                            if day > rain_record[rains[i]]:
                                res[day] = rains[i]
                                del rain_record[rains[i]]
                                dry_day.remove(day)
                                break
                    if rains[i] in rain_record:
                        return []                            
                rain_record[rains[i]] = i
            else:
                dry_day.append(i)

        while dry_day:
            res[dry_day.pop()] = 1

        return res
    

from bisect import bisect_left
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]: #O(nlogn)
        res = [-1] * len(rains)
        rain_record = {}
        dry_day = []

        for i in range(len(rains)):
            if rains[i] > 0:
                if rains[i] in rain_record:
                    if not dry_day:
                        return []
                    else:
                        idx = bisect_left(dry_day, rain_record[rains[i]])
                        if idx == len(dry_day): return []
                        res[dry_day[idx]] = rains[i]
                        del rain_record[rains[i]]
                        dry_day.pop(idx)
                    if rains[i] in rain_record:
                        return []                            
                rain_record[rains[i]] = i
            else:
                dry_day.append(i)

        while dry_day:
            res[dry_day.pop()] = 1

        return res