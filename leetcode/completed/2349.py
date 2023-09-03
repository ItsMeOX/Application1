from collections import defaultdict
from heapq import heappop, heappush

class NumberContainers:

    def __init__(self):
        self.indices = defaultdict(list) # number: heap(indices)
        self.index_mapper = {} # index: number

    def change(self, index: int, number: int) -> None:
        self.index_mapper[index] = number
        heappush(self.indices[number], index)

    def find(self, number: int) -> int:
        while self.indices[number] and self.index_mapper[self.indices[number][0]] != number:
            heappop(self.indices[number])
        if not self.indices[number]:
            return -1
        return self.indices[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)