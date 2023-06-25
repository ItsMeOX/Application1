class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dp = [0] * (len(pressedKeys)+1)
        dp[0] = 1
        MOD = 10 ** 9 + 7

        for i in range(1, len(pressedKeys)+1):
            dp[i] += dp[i-1]
            if i-1 - 1 >= 0 and pressedKeys[i-1-1] == pressedKeys[i-1]:
                dp[i] += dp[i-2]
            if i-1 - 2 >= 0 and pressedKeys[i-1-2] == pressedKeys[i-1-1] == pressedKeys[i-1]:
                dp[i] += dp[i-3] 
            if pressedKeys[i-1] in '79' and i-1 - 3 >= 0 and pressedKeys[i-1-1] == pressedKeys[i-1-2] == pressedKeys[i-1-3] == pressedKeys[i-1]:
                dp[i] += dp[i-4]
            dp[i] %= MOD
        
        return dp[-1]
    
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dp = [0] * (len(pressedKeys)+1)
        dp[0] = 1
        MOD = 10 ** 9 + 7

        for i in range(1, len(pressedKeys)+1):
            dp[i] += dp[i-1]
            if i-2 >= 0 and pressedKeys[i-2] == pressedKeys[i-1]:
                dp[i] += dp[i-2]
            if i-3 >= 0 and pressedKeys[i-3] == pressedKeys[i-2] == pressedKeys[i-1]:
                dp[i] += dp[i-3] 
            if i-1 - 3 >= 0 and pressedKeys[i-1] in '79' and pressedKeys[i-2] == pressedKeys[i-3] == pressedKeys[i-4] == pressedKeys[i-1]:
                dp[i] += dp[i-4]

            dp[i] %= MOD

        return dp[-1]
    