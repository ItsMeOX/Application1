class Solution:
    def minOperations(self, n: int) -> int:
        # [1]
        # [1, 3]
        # [1, 3, 5]
        # [1, 3, 5, 7]
        # [1, 3, 5, 7, 9]
        # [1, 3, 5, 7, 9, 11]
        res = 0
        # case len is odd:
        if n % 2 == 1:
            for i in range(1, (n-1)//2 + 1):
                res += i * 2
        # case len is even:
        else:
            temp = 1
            for i in range(1, n//2 + 1):
                res += temp
                temp += 2

        return res
    
# can use ap formula