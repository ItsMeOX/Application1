from math import factorial
prev = 0
for i in range(1, 200+1):
    x = factorial(i)
    trailing = 0
    while x % 10 == 0:
        trailing += 1
        x //= 10
    if trailing == prev + 2: print(f"two: {i}")
    prev = trailing
    print(i, trailing)


# 10 makes a zero, 10 = 5 * 2,
# as there are more factors of 2 than of 5, we will take how many factors of 
# 5 are there to pair with 2 to make 10.
# For example: 
# 5! = 5*4*3*2*1, we can pair 5 with 2, so trailing zero = 1.
# 10! = 10*...*5...*2, we can pair 5 with 2 and 10 with 2, trailing zero = 2.
# 25! = 25*...*20...*15...*10...*5...*2, 
# notice that 25=5*5, 5*5*2=50 and 5*2*5*2=100 both have trailing zeroes,
# so every 25, we will have extra 1 trailing zero.
# Hence, every 5^x, we will have an extra 1 increment of trailing zero.
# 1~4: 0
# 5~9: 1
# 10~14: 2
# 15~19: 3
# 20~24: 4
# 25~29: 6
# ...

# Through observation: 
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return (n // 5 + n // 25 + n // 125 + n // 625 + n // 3125)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            res += n // 5
            n //= 5
        
        return res