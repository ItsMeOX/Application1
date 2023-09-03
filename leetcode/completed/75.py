from typing import List

# Two pass solution: counting sort.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = [0, 0, 0]
        for num in nums:
            counter[num] += 1
        
        pointer = 0
        for i in range(len(nums)):
            while not counter[pointer]:
                pointer += 1
            nums[i] = pointer
            counter[pointer] -= 1

# quicksort 3-way partition (from a post from leetcode)
# +------+---------+-------------+-------+
# |  <p  |  =p     |  unseen .  |   > p  |
# +------+---------+------------+--------+
#         ↑          ↑           ↑
#         left       i           right 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, i, right = 0, 0, len(nums)-1

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1