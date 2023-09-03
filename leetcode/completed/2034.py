from heapq import heappop, heappush

# Initialize a min and max heap, which stores (price, timeStamp) 
# Initialize a dictionary which key is timeStamp and value is latest price.
# Initialize a variable 'latest' which is the latest time.

# Every we perform 'update', set 'latest' to latest timeStamp. Also push (price, timeStamp) into min and max heap.

# To get minimum / maximum, we check if the latest price of timeStamp we got from heap is updated or not, if not then pop the staled 
# price from heap and continue check for the next minimum / maximum.
# If it is updated then just return the minimum / maximum price.

# To get 'current', just get price from mapper using 'latest' variable as key.

class StockPrice:

    def __init__(self):
        self.latest = -1
        self.maxHeap = [] # price, timestamp
        self.minHeap = []
        self.mapper = {}

    def update(self, timestamp: int, price: int) -> None:
        self.latest = max(self.latest, timestamp)
        self.mapper[timestamp] = price
        heappush(self.maxHeap, (-price, timestamp))
        heappush(self.minHeap, (price, timestamp))

    def current(self) -> int:
        return self.mapper[self.latest]

    def maximum(self) -> int:
        while self.mapper[self.maxHeap[0][1]] != -self.maxHeap[0][0]:
            heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        while self.mapper[self.minHeap[0][1]] != self.minHeap[0][0]:
            heappop(self.minHeap)
        return self.minHeap[0][0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()