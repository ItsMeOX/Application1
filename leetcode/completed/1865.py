from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.counter1 = {}
        self.counter2 = {}

        for n in nums1:
            self.counter1[n] = self.counter1.get(n, 0) + 1
        for n in nums2:
            self.counter2[n] = self.counter2.get(n, 0) + 1

    def add(self, index: int, val: int) -> None:
        self.counter2[self.nums2[index]] -= 1
        self.counter2[val+self.nums2[index]] = self.counter2.get(val+self.nums2[index], 0) + 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        res = 0
        for key in self.counter1:
            if tot - key in self.counter2:
                res += self.counter2[tot-key] * self.counter1[key]
        
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)