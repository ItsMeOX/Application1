class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        a = [(str.count('0'), str.count('1')) for str in strs]
        memo = {}

        def dfs(i, zeros, ones):
            if zeros > m or ones > n:
                return float('-inf')

            if i == len(strs):
                return 0
            
            if (i, zeros, ones) in memo:
                return memo[(i, zeros, ones)]

            memo[(i, zeros, ones)] = max(dfs(i+1, zeros, ones), dfs(i+1, zeros+a[i][0], ones+a[i][1])+1)
            return memo[(i, zeros, ones)]

        return dfs(0, 0, 0)

sol = Solution()
print(sol.findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], m = 9, n = 80))