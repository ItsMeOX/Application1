class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        seen = set()

        def dfs(cur, visited):

            for j in range(len(tiles)):
                if j in visited: continue
                # not take
                visited.add(j)
                if cur not in seen:
                    seen.add(cur)
                dfs(cur, visited)
                visited.remove(j)


                # take
                visited.add(j)
                cur += tiles[j]
                if cur not in seen:
                    seen.add(cur)
                dfs(cur, visited)
                visited.remove(j)
                cur = cur[:-1]

        dfs('', set())
    
        return len(seen) - 1
    
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        seen = set()

        def dfs(cur, remain):
            seen.add(cur)
            for i in range(len(remain)):
                dfs(cur + remain[i], remain[:i]+remain[i+1:])
        
        dfs('', tiles)

        return len(seen) - 1
    
# If we take current letter, then counter[letter] -= 1,
# then loop through the whole dictionary again,
# we can only choose the character if counter[letter] > 0.
# After exploring possibilities after adding current, we counter[letter] += 1,
# which means unusing current letter.

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        counter = {}

        for t in tiles:
            counter[t] = counter.get(t, 0) + 1

        def dfs():
            nonlocal res
            res += 1
            for key in counter:
                if counter[key]:
                    counter[key] -= 1
                    dfs() 
                    counter[key] += 1

        res = 0
        dfs()

        return res - 1