# Initialize two arrays 'tell' and 'forgets' where 
# tell[i] denotes how many ppl will spread the secret at day i,
# forgets[i] denotes how many ppl will forget about the secret day i.
# For i th day, 
# active teller will increase / decrease by (tell[i] - forgets[i]),
# res will increase / decrease by (active_teller of day i - forgets[i]),
# we will have to update i+forget th day and i+delay th with active_teller.

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        res = 1
        active_teller = 0
        tell = [0] * (max(forget, delay)+n)
        tell[delay] = 1
        forgets = [0] * (max(forget, delay)+n)
        forgets[forget] = 1
        MOD = 10 ** 9 + 7

        for i in range(n):
            active_teller += tell[i] - forgets[i]
            res += active_teller - forgets[i]
            forgets[i+forget] += active_teller
            tell[i+delay] += active_teller

        return res % MOD