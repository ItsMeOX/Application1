class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        d = {}
        A , B = 0 , 0

        for s_letter , g_letter in zip(secret, guess):
            if s_letter == g_letter:
                A += 1
            else:

                d[s_letter] = d.get(s_letter, 0) + 1 # better than defaultdict in terms of memory
                d[g_letter] = d.get(g_letter, 0) - 1
                

                
                if d[s_letter] < 1:
                    B += 1
                if d[g_letter] > -1:
                    B += 1

        return f'{A}A{B}B'

        

sol = Solution()
secret = "1123"
guess  = "0111"
print(sol.getHint(secret, guess))