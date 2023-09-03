
# We initialize our dp states as following:
# 1. i: current index at playlist[i], 1 <= i <= goal
# 2. unplayed: number of unplayed song

# Base cases:
# 1. unplayed < 0 just does not make sense, so return 0.
# 2. Here i set if i == goal+1 as base case because that we will count less if i == goal and we can replay song, we will less count the replay song part.
#    So if i == goal+1 and unplayed == 0, which means that there are exactly n songs played, then we return 1, otherwise 0.

# State transitions:
# 1. Add new song: i+1, unplayed song - 1, 
#    at that position, we can choose 'unplayed' number of song, so multiply by 'unplayed' number of song.
# 2. Choose old song: i+1, unplayed song does not change,
#    at that position, the number of song we can choose are (num of chosen song - k) = (n-unplayed) - k.

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        memo = {}

        def dfs(i, unplayed):
            if (i, unplayed) in memo:
                return memo[(i, unplayed)]

            if unplayed < 0:
                return 0

            if i == goal+1:
                if unplayed == 0:
                    return 1
                return 0
            
            # add new song
            res = dfs(i+1, unplayed-1) * unplayed
        
            #replay song
            if (n - unplayed) >= k:
                res += dfs(i+1, unplayed) * (n-unplayed-k)
            
            memo[(i, unplayed)] = res % MOD

            return memo[(i, unplayed)]
        
        return dfs(1, n) % MOD