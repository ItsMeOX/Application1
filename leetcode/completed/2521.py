from math import sqrt
from typing import List

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num

        prime_factors = set()

        def isPrime(num):
            for i in range(2, int(sqrt(num))+1):
                if num % i == 0:
                    return False
            return True

        while product > 1:
            for i in range(2, int(sqrt(product))+1):
                if product % i == 0 and isPrime(i):
                    prime_factors.add(i)
                    product //= i
                    break
            if isPrime(product):
                prime_factors.add(product)
                break                   

        return len(prime_factors)
    
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime_factors = set()

        for num in nums:
            temp = 2
            while temp * temp <= num:
                while num % temp == 0:
                    num //= temp
                    prime_factors.add(temp)
                temp += 1
            if num > 1:
                prime_factors.add(num)

        return len(prime_factors)

sol = Solution()
print(sol.distinctPrimeFactors(nums = [2,4,3,7,10,6]))