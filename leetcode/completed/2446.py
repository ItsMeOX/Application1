from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def getTime(event):
            h, m = [int(t) for t in event.split(":")]
            return h * 60 + m
        
        event1_start = getTime(event1[0])
        event1_end   = getTime(event1[1])

        event2_start = getTime(event2[0])
        event2_end   = getTime(event2[1])

        if event1_end >= event2_end >= event1_start:
            return True
        
        if event2_end >= event1_end >= event2_start:
            return True

        return False