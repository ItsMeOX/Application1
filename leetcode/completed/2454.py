from heapq import heappush, heappop
from typing import List

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]: #O(nlogn)
        n = len(nums)
        res = [-1] * n

        normal_heap = []
        first_heap = []

        for i in range(n):
            while first_heap and first_heap[0][0] < nums[i]:
                _, j = heappop(first_heap)
                res[j] = nums[i]
            while normal_heap and normal_heap[0][0] < nums[i]:
                heappush(first_heap, heappop(normal_heap))
            heappush(normal_heap, (nums[i], i))

        return res
    
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]: # O(n)
        n = len(nums)
        res = [-1] * n

        first_stack = []
        second_stack = []

        for i in range(n):
            temp = []
            while second_stack and nums[i] > nums[second_stack[-1]]:
                res[second_stack.pop()] = nums[i]
            while first_stack and nums[i] > nums[first_stack[-1]]:
                temp.append(first_stack.pop())
            for t in temp[::-1]:
                second_stack.append(t)
            first_stack.append(i)

        return res