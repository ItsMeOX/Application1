from typing import List
from heapq import heappop, heappush

# Sort the trips by their starting time first.
# Initialize variable 'cur_cap' which indicates current amount of ppl in car.
# Initialize a min heap 'drop_off' which has the format (leaving time, amount of ppl).
# For each fetching, check if anyone is leaving, if true then let them leave first,
# then fetch the current passenger.
# Check if after fetching the current passenger, cur_cap > capacity?
# If true then return False.
# Then, heappush (leaving time, this passenger amount) into 'drop_off'.
# Note that we have to use heap here instead of queue because the leaving time is not in increasing order.

# O(nlogn)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cur_cap = 0
        trips.sort(key=lambda e: e[1])
        drop_off = []

        for cnt, src, dst in trips:
            while drop_off and drop_off[0][0] <= src:
                _, leaving = heappop(drop_off)
                cur_cap -= leaving
            cur_cap += cnt
            if cur_cap > capacity: return False
            heappush(drop_off, (dst, cnt))
        
        return True
    
# Becuz dst are 0 <= dst <= 1000, we can use this method as well.
# O(n)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001
        for cnt, src, dst in trips:
            stops[src] += cnt
            stops[dst] -= cnt
        
        cur_cap = 0
        for stop in stops:
            cur_cap += stop
            if cur_cap > capacity: return False
        
        return True