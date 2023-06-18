class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]: #O(len(nums1) * len(nums2))
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            while (j < len(nums2)):
                if nums2[j] > nums1[i]:
                   res[i] = nums2[j]
                   break
                j += 1

        return res
    
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]: #O(len(nums1) + len(nums2))
        stack = []
        mapping = {}

        for num in nums2:
            while stack and stack[-1] < num:
                mapping[stack.pop()] = num 
            stack.append(num)

        return [mapping.get(i, -1) for i in nums1]