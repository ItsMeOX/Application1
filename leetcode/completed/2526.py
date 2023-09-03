class DataStream:

    def __init__(self, value: int, k: int):
        self.cur_k = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.cur_k += 1
        else:
            self.cur_k = 0
        return self.cur_k >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)