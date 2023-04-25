class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        q = []

        row_len = len(mat)
        col_len = len(mat[0])
        visited = [[0 for _ in range(col_len)] for _ in range(row_len)]

        def bfs(mat, row, col):
            if mat[row][col] == 0:
                return
            
            if visited[row][col] == 1:
                return
                
            visited[row][col] = 1

            while q:
                row, col = q.pop(0)
                current_value = mat[row][col]

                if visited[row][col] == 1:
                    if mat[row][col] > current_value + 1:
                        visited[row][col] = 0
                        q.append([row,col])
            

        for row in mat:
            for col in row:
                q.append([row,col])
                bfs(mat,row,col)
        
        return mat

mat = [[1,0,0],[0,1,0],[1,1,1]]

sol = Solution()
sol.updateMatrix()
