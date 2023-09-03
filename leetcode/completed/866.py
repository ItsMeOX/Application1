from math import sqrt

class Solution:
    def primePalindrome(self, n: int) -> int:
        if n == 1    : return 2
        if n % 1 == 0: n += 1 
        cache = []

        def isPrime(num):
            if cache:
                for prime in cache:
                    if num % prime == 0:
                        return False

            lower = cache[-1] if cache else 2
    
            for prime in range(lower, int(sqrt(num))+1):         
                if num % prime == 0:
                    return False
            cache.append(num)
            return True

        def isPalindrome(num):
            return str(num) == str(num)[::-1]
        
        while True:
            if isPalindrome(n) and isPrime(n):
                return n
            print(n)
            n += 2

sol = Solution()
print(sol.primePalindrome(101101))