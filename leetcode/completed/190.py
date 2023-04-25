class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            if n % 2 == 1:
                res <<= 1
                res += 1
            else:
                res <<= 1
            n >>= 1
        return res
    

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0

#         for _ in range(32):
#             res = (res<<1) + (1&n)
#             n >>= 1
#         return res

# class Solution:
#     def reverseBits(self, n):
#         n = bin(n)[2:]
#         n = '0'*( 32-len(n) ) + n
#         return int( n[::-1] ,2)