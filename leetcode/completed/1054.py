from collections import Counter
from typing import List
from heapq import heappop, heappush

# Initialize a max heap with (counter[i], i), for i from 0 ~ barcode.length-1.
# Pop 2 number from heap,
# then add the two numbers to res alternatively.
# Check if counter[first number] < counter[front number],
# if true then swap first number and front number.

# bar: [1,1,1,1,2,2,3,3]
# res: [1,2,1,2,1,3,1,3]

# bar: [2,2,3,3,3,7,7,7,7]
# res: [7,3,7,3,7,2,7,2,3]

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        heap = []
        res = []

        for key in counter:
            heappush(heap, (-counter[key], key))

        c1, n1 = heappop(heap)
        if heap:
            c2, n2 = heappop(heap)
        else:
            c2, n2 = 0, 0
        for _ in range(len(barcodes)):
            if c1:
                res.append(n1)
                c1 += 1

            if heap and c1 > heap[0][0]:
                temp = (c1, n1)
                c1, n1 = heappop(heap)
                heappush(heap, temp)

            if c2:
                res.append(n2)
                c2 += 1
            
            if heap and not c2:
                c2, n2 = heappop(heap)

        return res

# Fill the most common num into res with gap of 1 first.
# After filling, just fill the remaining in slot with gap of 1.

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        res = [0] * len(barcodes)
        heap = []
        i = 0

        for key in counter:
            heappush(heap, (-counter[key], key))
        
        while heap:
            count, num = heappop(heap)
            for _ in range(-count):
                if i >= len(barcodes): i = 1
                res[i] = num
                i += 2
        
        return res
            