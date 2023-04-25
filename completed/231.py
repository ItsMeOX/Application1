class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n and (n & n-1) == 0

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False
        
#         while n%2 == 0:
#             n //= 2

#         return True if n == 1 else False
    



sol = Solution()
print(sol.isPowerOfTwo(0))