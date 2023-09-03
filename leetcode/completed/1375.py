from typing import List

# Keep a hash set that records flipped bulb j which is > i.
# If flipped bulb j <= i, then left += 1
# If left == i and no right bulb are lit, then res++.

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        left = 0 # 1's at left
        n = len(flips)
        res = 0
        right_dic = set()

        for i in range(1, n+1):
            if i in right_dic:
                right_dic.remove(i)
                left += 1

            if flips[i-1] <= i:
                left += 1
            else:
                right_dic.add(flips[i-1])
            
            if left == i and len(right_dic) == 0:
                res += 1

        return res
    
# Keep track of the rightmost bulb flipped,
# if rightmost bulb flipped == i, that means all bulbs <= i must be lit.

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        rightmost = 0
        n = len(flips)
        res = 0

        for i in range(1, n+1):
            rightmost = max(rightmost, flips[i-1])
            if rightmost == i:
                res += 1

        return res