from typing import List

# See below.

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        pre = suf = sub_max = 0
        total_sum = 0
        temp = 0
        sub_temp = 0
        MOD = 10 ** 9 + 7

        for num in arr:
            total_sum += num
            temp += num
            sub_temp += num
            if sub_temp < 0:
                sub_temp = 0
            pre = max(pre, temp)
            sub_max = max(sub_max, sub_temp)

        temp = 0
        for i in range(len(arr)-1, -1, -1):
            temp += arr[i]
            suf = max(suf, temp)

        if k == 1:
            return max(0, total_sum, pre, suf)

        if total_sum < 0:
            return max(0, pre, suf, suf+pre, sub_max)
        else:
            return (max(total_sum, suf) + (total_sum * (k-2)) % MOD + max(total_sum, pre)) % MOD
        
# Initialize a function 'findMaxSubarray' which utilizes Kadane's algorithm to find maximum subarray.
# There are 3 cases for this problem:
# 1. if k is 1           , then just simply find the maximum subarray.
# 2. if sum of array <= 0, then we need to find the maximum subarray of k = 2.
# 3. if sum of array >  0, then for the 2 ~ k-1 iterations, we will just add the total sum of array. 
#                          For k = 1, we need find the largest ending segment, 
#                          and for k = last, we need to find the largest starting segment.
#                          This is the same for finding maximum subarray of k = 2.

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def findMaxSubarray(arr):
            res = 0
            temp = 0
            for x in arr:
                temp += x
                if temp < 0:
                    temp = 0
                if res < temp:
                    res = temp
            
            return res
        
        sums = sum(arr)
        MOD = 10 ** 9 + 7

        if k == 1:
            return findMaxSubarray(arr) % MOD
        if sums <= 0:
            return findMaxSubarray(arr+arr) % MOD
        
        # sums > 0 and k >= 2
        return (findMaxSubarray(arr+arr) + sums * (k-2)) % MOD