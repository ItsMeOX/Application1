class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        res = 0
        for row in grid:
            for i in range(len(grid[0])):
                idx = 0
                for j in range(len(grid)):
                    if grid[j][i] == row[j]:
                        idx += 1
                    else:
                        break
                if idx == len(grid):
                    res += 1
        
        return res
    
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        dic = {}
        res = 0
        for row in grid:
            temp = ""
            for n in row:
                temp += str(n)
                temp += "-"
            dic[temp] = dic.get(temp, 0)+1
        
        for i in range(len(grid[0])):
            temp = ""
            for j in range(len(grid)):
                temp += str(grid[j][i])
                temp += "-"
            if temp in dic:
                res += dic[temp]

        return res
    
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        dic = {}
        res = 0
        for row in grid:
            dic[tuple(row)] = dic.get(tuple(row), 0) + 1
        for col in zip(*grid):
            if col in dic:
                res += dic[col]
        return res
    
sol = Solution()
print(sol.equalPairs([[11,1],[1,11]]
))