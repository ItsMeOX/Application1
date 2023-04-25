class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        first , sec , third  = 0 , 1 , 1 

        for _ in range(n-2):
            temp = first + sec + third
            first = sec
            sec = third
            third = temp

        return third


# class Solution:
#     def tribonacci(self, n: int) -> int:
#         memo = {0:0, 1:1, 2:1}
        
#         def recursion(i):
#             if i < 0:
#                 return 0

#             if i in memo:
#                 return memo[i]

#             res = recursion(i-1) + recursion(i-2) + recursion(i-3)
#             memo[i] = memo.get(i, res)

#             return res

#         return recursion(n)