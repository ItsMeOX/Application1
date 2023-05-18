class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(res[i-1][j-1] + res[i-1][j])
            res.append(temp)
        return res

        # res = [[1]*i for i in range(1, numRows+1)]
        # for i in range(2, numRows):
        #     for j in range(1, i):
        #         res[i][j] = res[i-1][j-1] + res[i-1][j]

        # return res

sol = Solution()
print(sol.generate(7))