from typing import List

# Initialize two dictionaries which stores the frequency of each element in nums1 and nums2.
# Then we iterate i from 0 to len(arr1), for each iteration of i, we iterate j from 0 to len(arr2).
# if num1 ^ 2  / num2 is in counter of nums2, then add counter[num1^2 / num2] to res, if num1^2/nums2 is the same as nums2, we have -1.
# Repeat this process for nums2 array too.
# As we have repeated our calculation twice, we have to /2 our res at last. 

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = {}
        counter2 = {}

        for num in nums1:
            counter1[num] = counter1.get(num, 0) + 1
        for num in nums2:
            counter2[num] = counter2.get(num, 0) + 1
        
        def calc(arr1, arr2, counter):
            res = 0
            for num1 in arr1:
                num1 = num1 * num1
                for num2 in arr2:
                    if num1 % num2 == 0 and num1 // num2 in counter:
                        res += counter[num1 // num2] - (num1 // num2 == num2)
            return res
        
        res = (calc(nums1, nums2, counter2) + calc(nums2, nums1, counter1)) // 2

        return res