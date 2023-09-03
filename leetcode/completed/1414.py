# Naive approach: 
# generate fibonacci array until arr[-1] > k,
# Then iterate from last to first and greedily subtrack k by arr[i] until k = 0.

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k <= 2: return 1

        arr = [1,1]

        while arr[-1] < k:
            arr.append(arr[-1] + arr[-2])
        
        res = 0
        sums = 0
        for i in range(len(arr)-1, -1, -1):
            if sums + arr[i] <= k:
                sums += arr[i]
                res += 1
            if sums == k:
                return res
            
        # Optimization: using binary search
        # res = 0
        # while k:
        #     index = bisect_right(arr, k) - 1
        #     k -= arr[index]
        #     res += 1
        # return res

# O(1) solution
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k <= 2: return 1

        a, b = 1, 1
        
        while b < k:
            a, b = a+b, a
        
        res = 0
        while k:
            if a <= k:
                k -= a
                res += 1
            
            a, b = b, a-b
        
        return res