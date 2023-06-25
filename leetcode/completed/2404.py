from typing import List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt = {}
        for num in nums:
            if num % 2 == 0:
                cnt[num] = cnt.get(num, 0) + 1

        res = -1
        max_ = 0
        for key in cnt.keys():
            if cnt[key] > max_:
                res = key
                max_= cnt[key]
            elif cnt[key] == max_ and key < res:
                res = key
                max_= cnt[key]

        return res