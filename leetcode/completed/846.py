from typing import List
from heapq import heapify, heappop

# O(len(hand) ^ 2)
# If hand cannot be distributed into group which length is exactly groupSize, return false.
# Initialize a counter dictionary and stores the frequency of each number in arr 'hand'.
# Iterate for total number of group that can be formed, 
# starting from current minimum value of ungrouped value for 'hand', 
# if current_min_val + k is not in 'counter' (or its value is 0), then return false,
# else decrease the count of that number.
# Return true at last.

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False 

        counter = {}

        for h in hand:
            counter[h] = counter.get(h, 0) + 1

        for _ in range(len(hand) // groupSize):
            cur_min = min(counter.keys())
            counter[cur_min] -= 1
            if not counter[cur_min]:
                del counter[cur_min]
            
            for i in range(1, groupSize):
                if cur_min+i not in counter:
                    return False
                counter[cur_min + i] -= 1
                if not counter[cur_min + i]:
                    del counter[cur_min + i]
        
        return True

# Optimization:
# Instead of getting current minimum number from 'counter' with min() function, which requires O(len(counter)) time,
# we can heapify keys of 'counter' and we can access the current minimum number at O(1) time, 
# although popping requires O(log(len(counter))) time, it is still better than O(len(counter)).

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False 

        counter = {}

        for h in hand:
            counter[h] = counter.get(h, 0) + 1

        heap = list(counter.keys())
        heapify(heap)

        while heap:
            cur_min = heap[0]
            if not counter[cur_min]:
                heappop(heap)
            else:
                for i in range(groupSize):
                    if cur_min+i not in counter or counter[cur_min+i] == 0:
                        return False
                    counter[cur_min + i] -= 1

        return True