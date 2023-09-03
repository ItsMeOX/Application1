from typing import List

# Initialize a 2D list (grid), where grid[r][c] is 1 if it is digged, or 0 if not digged.
# Then for each artifact, iterate through all the grid covered by the artifact,
# if all grid covered are digged, then res += 1.

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(n)]
        for r, c in dig:
            grid[r][c] = 1
        
        res = 0
        for r1, c1, r2, c2 in artifacts:
            valid = True
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    if not grid[r][c]:
                        valid = False
                        break
                if not valid: break
            res += valid
        
        return res