from typing import List
from math import sqrt

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        res = 0
        n = len(nums)
        
        def isPrime(num):
            if num == 1: return False
            for i in range(2, int(sqrt(num)+1)):
                if num % i == 0:
                    return False
            return True

        col = 0
        row = 0
        while col < n:
            if nums[row][col] > res and isPrime(nums[row][col]):
                res = max(res, nums[row][col])
            row += 1
            col += 1

        col = n - 1
        row = 0
        while col > -1:
            if nums[row][col] > res and isPrime(nums[row][col]):
                res = max(res, nums[row][col])
            row += 1
            col -= 1
        
        return res

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        res = 0
        n = len(nums)
        
        def isPrime(num):
            if num == 1: return False
            for i in range(2, int(sqrt(num)+1)):
                if num % i == 0:
                    return False
            return True

        for i in range(n):
            if nums[i][i] > res and isPrime(nums[i][i]):
                res = max(res, nums[i][i])
            if nums[i][-i-1] > res and isPrime(nums[i][-i-1]):
                res = max(res, nums[i][-i-1])
        
        return res

