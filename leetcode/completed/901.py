
# Build a list with tuple (price, index of previous larger number).
# For every query, if price list[i] <= current price, 
# jump to prev larger number index of list[i].

class StockSpanner:

    def __init__(self):
        self.record = [] # (price, prev larger index)

    def next(self, price: int) -> int:
        if not self.record:
            self.record.append((price, -1))
            return 1

        i = len(self.record) - 1
        while i >= 0 and self.record[i][0] <= price:
            i = self.record[i][1]
        self.record.append((price, i))
        return len(self.record) - i - 1


# Basically monotonic stack.
class StockSpanner:

    def __init__(self):
        self.record = []

    def next(self, price: int) -> int:
        res = 1
        while self.record and self.record[-1][0] <= price:
            res += self.record.pop()[1]
        
        self.record.append((price, res))
        return res

print(ord('z'))