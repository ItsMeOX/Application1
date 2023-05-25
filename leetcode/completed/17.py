class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        pair = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []

        def dfs(i, comb):
            if i == len(digits):
                res.append(comb)
            else:
                for letter in pair[digits[i]]:
                    dfs(i+1, comb + letter)

        dfs(0, '')            

        
        return res

sol = Solution()
print(sol.letterCombinations("2342"))