class Solution:
    def secondHighest(self, s: str) -> int:
        sorted_num = sorted([int(c) for c in set(s) if c.isdigit()], reverse=True)

        return sorted_num[1] if len(sorted_num) > 1 else -1
    
class Solution:
    def secondHighest(self, s: str) -> int:
        largest, larger = -1, -1

        for c in s:
            if not c.isdigit():
                continue
            c = int(c)
            if c > largest:
                largest, larger = c, largest
            elif larger < c < largest: # can do this instead of elif c != largest and c < largest.
                larger = c
            
        return larger