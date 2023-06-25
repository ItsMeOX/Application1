from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        col = len(image[0])
        row = len(image)

        for i in range(row):
            for j in range(col // 2):
                image[i][j], image[i][col-1-j]  = image[i][col-1-j], image[i][j]

        for i in range(row):
            for j in range(col):
                if image[i][j]:
                    image[i][j] = 0
                else:
                    image[i][j] = 1

        return image
    
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1-col for col in row][::-1] for row in image]

sol = Solution()
print(sol.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
# [[1,0,0],[0,1,0],[1,1,1]]