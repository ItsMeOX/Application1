class SnapshotArray:

    def __init__(self, length: int):
        self.storage = [[(0,0)] for _ in range(length)]
        self.curIdx = 0

    def bSearch(self, idx, target):
        lo, hi = 0, len(self.storage[idx])
        while (lo < hi):
            m = (lo+hi)//2
            if self.storage[idx][m][0] <= target:
                lo = m + 1
            else:
                hi = m
        return lo - 1

    def set(self, index: int, val: int) -> None:
        self.storage[index].append((self.curIdx, val))

    def snap(self) -> int:
        self.curIdx += 1
        return self.curIdx - 1 

    def get(self, index: int, snap_id: int) -> int:
        idx = self.bSearch(index, snap_id)
        return self.storage[index][idx][1]




# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)