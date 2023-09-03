from typing import List

# Naive approach:
# Keep two pointers left and right,
# and compute the maximum values for every subarray arr[left: right+1], which means swapping the values of two arrays in the range [left, right].
# This will be O(N^2), 
# but we can find maximum sum of subarray using Kadane's algorithm in O(N) time.

# Using Kadane's algorithm here.
# Define two arrays profit_a and profit_b,
# profit_a[i] = maximum subarray to swap nums2 from any index from 0 ~ i to i, same for profit_b.
# Compute the largest subarray values using Kadane's algorithm,
# and add the largest subarray value (minimum 0) to sum of each array and take the maximum among the two values.

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        profit_a = [0]
        profit_b = [0]

        for i in range(n):
            profit_a.append(max(0, profit_a[-1] + nums2[i] - nums1[i]))
            profit_b.append(max(0, profit_b[-1] + nums1[i] - nums2[i]))

        return max(max(profit_a) + sum(nums1), max(profit_b) + sum(nums2))
    

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        max_profit1 = 0
        prev_profit1 = 0
        max_profit2 = 0
        prev_profit2 = 0

        for i in range(n):
            prev_profit1 = max(0, prev_profit1 + nums2[i] - nums1[i])
            prev_profit2 = max(0, prev_profit2 + nums1[i] - nums2[i])
            max_profit1 = max(prev_profit1, max_profit1)
            max_profit2 = max(prev_profit2, max_profit2)

            # profit_a.append(max(0, profit_a[-1] + nums2[i] - nums1[i]))
            # profit_b.append(max(0, profit_b[-1] + nums1[i] - nums2[i]))

        return max(max_profit1 + sum(nums1), max_profit2 + sum(nums2))