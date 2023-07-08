class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0

        # check for T
        count = 0
        k_used = 0 
        left = 0
        for c in answerKey:
            if c == 'F':
                k_used += 1
                if k_used > k:
                    while answerKey[left] == 'T':
                        left += 1
                        count -= 1
                    left += 1
                    count -= 1
            count += 1
            res = max(res, count)

        # check for F
        count = 0
        k_used = 0
        left = 0 
        for c in answerKey:
            if c == 'T':
                k_used += 1
                if k_used > k:
                    while answerKey[left] == 'F':
                        left += 1
                        count -= 1
                    left += 1
                    count -= 1
            count += 1
            res = max(res, count)

        return res

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0

        def check(x):
            nonlocal res
            k_used = 0 
            left = 0
            for right, c in enumerate(answerKey):
                if c == x:
                    k_used += 1
                    if k_used > k:
                        while answerKey[left] != x:
                            left += 1
                        left += 1
                res = max(res, right - left + 1)

        check('T')
        check('F')

        return res


sol = Solution()
print(sol.maxConsecutiveAnswers(answerKey = "TTFTFFTTT", k = 2))