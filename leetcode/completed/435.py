from typing import List

# Sort intervals by starting time.
# Initialize a variable 'end' indicating the end number of current interval. (initially it is -inf)
# Iterate through intervals and check if starting time is >= current end.
# If it is >=, then update our end time without increasing res.
# Else, increase res. Also, if end time is earlier than current end time, update current end time to that end time.

# Key takeaway: greedily choose the shortest interval possible.

# Case 1: -----#####          -> update end time without increasing res.                  # = current interval, - = last interval
# Case 2: ------              -> do not update end time, but increase res.
#            #######
# Case 3: -------             -> update end time and increase res.
#           ###

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = -float('inf')
        res = 0

        for s, e in intervals:
            if s >= end:
                end = e
            else:
                if e < end:
                    end = e
                res += 1

        return res
