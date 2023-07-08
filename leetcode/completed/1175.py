from math import factorial

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        def countPrime(m):
            primes = []
            for i in range(2, m+1):
                isPrime = True

                for j in primes:
                    if i % j == 0:
                        isPrime = False
                        break
                if isPrime:
                    primes.append(i)
            return len(primes)

        primeCnt = countPrime(n)
        return (factorial(n-primeCnt) * factorial(primeCnt)) % MOD
    
sol = Solution()
print(sol.numPrimeArrangements(6))