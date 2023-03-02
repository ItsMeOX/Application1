class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        self.row , self.col = len(image) , len(image[0])
        self.targetColor = color
        self.color = image[sr][sc]
        self.visited = []
        self.dfs(image, sr, sc)
        return image

    def dfs(self, image, sr, sc):
        if image[sr][sc] == self.color and [sr,sc] not in self.visited:
            image[sr][sc] = self.targetColor    
            self.visited.append([sr,sc])
            if sr - 1 >= 0:
                self.dfs(image, sr - 1 , sc) 
            if sc + 1 < self.col:
                self.dfs(image, sr , sc + 1)
            if sr + 1 < self.row:
                self.dfs(image, sr + 1 , sc)
            if sc - 1 >= 0:
                self.dfs(image, sr , sc - 1)


