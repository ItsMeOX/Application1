class Solution:
    def average(self, salary: list[int]) -> float:
        sort = sorted(salary)[1:-1]
        return sum(sort)/len(sort)
    

# class Solution:
#     def average(self, salary: List[int]) -> float:
#         maxS , minS = sys.maxsize, -sys.maxsize
#         res = 0
#         for i in salary:
#             if i < maxS:
#                 maxS = i
#             if i > minS:
#                 minS = i
#             res += i
#         return (res - maxS - minS) / (len(salary) - 2)

# class Solution:
#     def average(self, salary: List[int]) -> float:
#         return sum(sorted(salary)[1:-1])/(len(salary)-2)