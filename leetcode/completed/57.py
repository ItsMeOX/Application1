from typing import List

# Iterate through the intervals list and find the insertion point for the newInterval.
# The insertion point will be at place where the starting time is larger than the starting time of newInterval.
# If we couldn't find any starting time that is larger than the starting time of newInterval, it means we should insert the new interval at last,
# so we append interval if new interval is not added.

# Then we iterate again to merge the intervals.
# To merge the intervals, append the first interval to 'res' list.
# From second interval, check if the starting time of current interval is larger than the starting time of last interval of 'res'.
# If yes, that means there is no overlapping between intervals, so just append the current interval to 'res'.
# If not, that means there is overlap and we update the ending time of last interval of 'res' to the latest time between last interval or 'res' and
# current interval.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        added = False

        for i in range(len(intervals)):
            start, end = intervals[i]
            if start > new_start:
                added = True
                intervals.insert(i, newInterval)
                break

        if not added:
            intervals.append(newInterval)

        for i in range(len(intervals)):
            start, end = intervals[i]
            if not res or res[-1][1] < start:
                res.append(intervals[i])
            elif res[-1][1] < end:
                res[-1][1] = end

        return res