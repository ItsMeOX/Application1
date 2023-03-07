class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def dfs(path, nums, count):
            if len(path) == k:
                res.append(path[:])
                return

            for val in nums[count:]: 

                path.append(val)
                count += 1
                dfs(path, nums, count)
                path.pop()


        res = []
        dfs([],[i for i in range(1,n+1)],0)
        return res
        
    
sol = Solution()
print(sol.combine(20,5))


# VERY VERY SLOW #
# class Solution:
#     def combine(self, n: int, k: int) -> list[list[int]]:
#         def dfs(path, nums, res):
#             if len(path) == k:
#                 res.append(path[:])
#                 return

#             for val in nums: 
#                 if path:
#                     if val <= path[-1]:
#                         continue
#                 path.append(val)
#                 dfs(path, nums, res)
#                 path.pop()


#         res = []
#         dfs([],[i for i in range(1,n+1)],res)
#         return res