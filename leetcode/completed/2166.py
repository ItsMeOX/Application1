class Bitset:

    def __init__(self, size: int):
        self.bits = set()
        self.size = size
        self.flipped = False

    def fix(self, idx: int) -> None:
        if self.flipped:
            if idx in self.bits:
                self.bits.remove(idx)
        else:
            if idx not in self.bits:
                self.bits.add(idx)

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if idx not in self.bits:
                self.bits.add(idx)    
        else:
            if idx in self.bits:
                self.bits.remove(idx)

    def flip(self) -> None:
        self.flipped = not self.flipped

    def all(self) -> bool:
        if self.flipped: return len(self.bits) == 0
        return len(self.bits) == self.size

    def one(self) -> bool:
        if self.flipped: return len(self.bits) != self.size
        return len(self.bits) > 0

    def count(self) -> int:
        if self.flipped: return self.size - len(self.bits)
        return len(self.bits)

    def toString(self) -> str:
        res = ''
        zero, one = '0', '1'
        if self.flipped: zero, one = '1', '0'
        for i in range(self.size-1, -1, -1):
            if i in self.bits:
                res += one
            else:
                res += zero
        return res[::-1]

# 00
# 01
# 00
# 00 
# 01

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()