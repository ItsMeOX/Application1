from typing import List

# [1,5]
# [0,0] -> [0,1] -> [0,2] -> [0,4] -> [1,4] -> [1,5], 5 operations needed.
# Here instead of building from [0,0] to [1,5], we can build from [1,5] to [0,0]

# From backward,
# notice that for every number in nums, if 
# num is odd, then we take one operation and subtract 1 for that num.
# After all numbers in nums are even, we will divide 2 for every numbers in nums, and this takes 1 operation too.

# flag here indicates whether there is still non-zero number in nums.
# While there is non-zero number in nums, we iterate through the nums array and check:
# if num is odd, we need one operation to make it even, so res += 1,
# then we will divide every number by 2 every iteration,
# after iteration we +1 to res.

# [1] -> [0] 1op(subtract 1) -> [0] 1op(divide 2) -> [0] 1op(divide2)
# [0] -> [0] 1op(divide 2)
# Because that we have extra 2 steps for case 1, so we have res-2
# Because that case 2, we have to max(0, res-2)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flag = True
        res = 0

        while flag:
            flag = False
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                if nums[i] & 1:
                    res += 1
                    nums[i] -= 1
                nums[i] //= 2
                flag = True
            res += 1
        
        return max(0, res - 2)

# Tips: If operations are only like +1, -1, *2, /2, then we might be able to use bit manipulation.  
# Optimization:
# Example: [1, 5]
# 1: 0b1
# 5: 0b101

# [0, 0] -> [0, 1] -> [0, 2] -> [0, 4] -> [0, 5] -> [1, 5]
# 0b0       0b0       0b00      0b000     0b0000    0b1000
# 0b0       0b1       0b10      0b100     0b1001    0b1001

# Notice that every '1' bit is a +1 operation,
# and we have to shift left (a mul by 2 operation) at most len(max(nums)) - 1.
# we also -2 here to subtract the '0b' length.
# So, we can just
# count the total '1' bit among all numbers and add the maximum left shift needed.

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        max_len = 0
        for num in nums:
            cur_bin = bin(num)
            max_len = max(max_len, len(cur_bin)-2)
            res += cur_bin.count('1')
        
        return res + max_len - 1