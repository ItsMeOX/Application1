class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
    
# class Solution:
#     memo = {}
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
        
#         if n in self.memo:
#             return self.memo[n]

#         res = self.fib(n-1) + self.fib(n-2)

#         self.memo[n] = res

#         return self.memo[n]


# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n

        
#         prev1 = 0
#         prev2 = 1
#         ans = 0

#         for _ in range(n-1):
#             ans = prev1 + prev2
#             prev1 = prev2
#             prev2 = ans

#         return ans