from typing import List

# Do backtrack here,
# base cases: 
# 1. if all nums are used (len(visited) == n), return true.
# 2. if i out of bound (i == n*2-1), return false.
# 
# Starting from i = 0, try every num from n to 1 (j),
# if res[i+j] != -1 which means occupied, then try next number,
# if j == 1, then just replace res[i] with 1 and continue to i+1.


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [-1] * (n*2-1)

        visited = set()

        def dfs(i):
            if len(visited) == n:
                return True
            
            if i == n*2-1:
                return False

            if res[i] != -1:
                return dfs(i+1)

            for j in range(n, 0, -1):
                if j in visited: continue
                res[i] = j

                if j == 1:
                    visited.add(j)
                    if dfs(i+1): return True
                    visited.remove(j)
                    res[i] = -1
                    continue

                if (i+j >= n*2-1):
                    res[i] = -1
                    continue

                if res[i+j] == -1:
                    visited.add(j)
                    res[i+j] = j
                    if dfs(i+1): return True
                    visited.remove(j)
                    res[i+j] = -1
                
                res[i] = -1

            return False

        dfs(0)

        return res
    
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [-1] * (n*2-1)

        visited = set()

        def dfs(i):
            if len(visited) == n:
                return True
            
            if i == n*2-1:
                return False

            if res[i] != -1:
                return dfs(i+1)

            for j in range(n, 0, -1):
                if j in visited: continue

                index1 = i
                index2 = i+j if j != 1 else i

                if index2 < n*2-1 and res[index2] == -1:
                    visited.add(j)
                    res[index1] = res[index2] = j
                    if dfs(i+1): return True
                    visited.remove(j)
                    res[index1] = res[index2] = -1
                
            return False

        dfs(0)

        return res

sol = Solution()
print(sol.constructDistancedSequence(30))