# class Solution:
#     def permute(self, nums: list[int]) -> list[list[int]]:
#         self.res = []
#         self.maxlen = len(nums)
#         for num in nums:
#             self.permute2([], nums,num)
#         return self.res

#     def permute2(self, current, nums, digit):
#         current = [i for i in current]
#         current.append(digit)
#         if len(current) == self.maxlen:
#             self.res.append(current)
#             return
#         for num in nums:
#             if num not in current:
#                 self.permute2(current, nums, num)    
        
class Solution:
    def permute(self, l: list[int]) -> list[list[int]]:
        def dfs(path, used):
            if len(path) == len(l):
                res.append(path[:])
                return
            
            for idx, val in enumerate(l):
                if used[idx]:
                    continue

                used[idx] = True
                path.append(val)

                dfs(path, used)

                used[idx] = False
                path.pop()

        res = []
        dfs([], [False]*len(l))
        return res


sol = Solution()
ans = sol.permute([0,1,2,4])
print(ans)