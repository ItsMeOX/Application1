from collections import deque
class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = deque()
        self.maxSize = maxSize
        self.length = 0

    def push(self, x: int) -> None:
        if self.length + 1 <= self.maxSize:
            self.length += 1
            self.arr.append(x)

    def pop(self) -> int:
        if self.length > 0:
            self.length -= 1
            return self.arr.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i == self.length:
                break
            self.arr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.maxSize = maxSize
        self.length = 0

    def push(self, x: int) -> None:
        if self.length + 1 <= self.maxSize:
            self.length += 1
            self.arr.append([x, 0])

    def pop(self) -> int:
        if self.length > 0:
            self.length -= 1
            val, inc = self.arr.pop()
            if self.length > 0:
                self.arr[-1][1] += inc
            return val + inc
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.length:
            self.arr[min(k, self.length)-1][1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)