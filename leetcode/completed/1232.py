class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if coordinates[1][0] - coordinates[0][0]:
            s = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        else:
            s = ''
        for i in range(2, len(coordinates)):
            if coordinates[i][0] - coordinates[i-1][0]:
                s2 = (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0])
            else:
                s2 = ''
            if s2 != s:
                return False 

        return True
    

sol = Solution()
print(sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
))