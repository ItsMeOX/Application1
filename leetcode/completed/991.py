from math import ceil

# Instead of starting from startValue to target,
# we can start from target to startValue.
# We keep dividing target by until it is <= startValue.
# if in the process target is odd, then the only option we have is just +1 (ceil here).
# If the target is less than startValue, then add all the way back to make it equal to startValue.
# For every operation of dividing and subtracting and adding, add 1 to res.

# start = 2, target = 100
# 100 -> 50 -> 25 -> 13 -> 7 -> 4 -> 2
#        (1)   (1)   (2)  (2)  (2)  (1) = 9 ops

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while target > startValue:
            if target & 1: res += 1
            res += 1
            target = ceil(target / 2)
        return startValue - target + res



# 10 1
# 5  2
# 3  