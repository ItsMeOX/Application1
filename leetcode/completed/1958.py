from typing import List

# bruh.

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m, n = len(board), len(board[0])
        board[rMove][cMove] = color

        def checkVertical(i, j):
            temp = []
            order = -1 if j < i else 1
            for pos in range(i, j, order):
                if board[pos][cMove] == '.':
                    break
                temp.append(board[pos][cMove])

                if len(temp) == 2 and temp[-1] == temp[0]:
                    return False
                if len(temp) > 2 and temp[-1] == temp[0]:
                    return True

            return False

        def checkHorizontal(i, j):
            temp = []
            order = -1 if j < i else 1
            for pos in range(i, j, order):
                if board[rMove][pos] == '.':
                    break
                temp.append(board[rMove][pos])

                if len(temp) == 2 and temp[-1] == temp[0]:
                    return False
                if len(temp) > 2 and temp[-1] == temp[0]:
                    return True

            return False

        res = []
        res.append(checkHorizontal(cMove, n))
        res.append(checkHorizontal(cMove, -1))
        res.append(checkVertical(rMove, m))                
        res.append(checkVertical(rMove, -1))                

        def checkDiagonal(x, y, dx, dy):
            temp = []
            while 0 <= x < n and 0 <= y < m and board[y][x] != '.':
                temp.append(board[y][x])
                x += dx
                y += dy

                if len(temp) == 2 and temp[-1] == temp[0]:
                    return False

                if len(temp) > 2 and temp[-1] == temp[0]:
                        return True

            return False


        res.append(checkDiagonal(cMove, rMove, 1, 1))
        res.append(checkDiagonal(cMove, rMove, -1, 1))
        res.append(checkDiagonal(cMove, rMove, 1, -1))
        res.append(checkDiagonal(cMove, rMove, -1, -1))

        return any(res)
        
# To check vertically / horizontally / diagonally, we can always use directions.

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1))
        m, n = len(board), len(board[0])

        def isLegal(x, y, dx, dy):
            length = 1
            x += dx
            y += dy

            while 0 <= x < n and 0 <= y < m:
                length += 1

                if board[y][x] == color:
                    return length >= 3
                
                if board[y][x] == '.':
                    return False
            
                x += dx
                y += dy

            return False
        
        for dx, dy in directions:
            if isLegal(cMove, rMove, dx, dy):
                return True
            
        return False 