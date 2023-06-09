# sys.stdout = open("sudoku.txt", "w")

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        possible = [[[] for _ in range(9)] for _ in range(9)]

        def checkV(number, col):
            for i in range(9):
                if board[i][col] == number:
                    return False
            return True

        def checkH(number, row):
            for i in range(9):
                if board[row][i] == number:
                    return False
            return True

        def checkS(number, row, col):
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for drow in range(3):
                for dcol in range(3):
                    if board[start_row + drow][start_col + dcol] == number:
                        return False
            return True

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                numbers = ['1','2','3','4','5','6','7','8','9']
                for drow in range(3):
                    for dcol in range(3):
                        if board[row+drow][col+dcol] != ".":
                            numbers.remove(board[row+drow][col+dcol])
                for drow in range(3):
                    for dcol in range(3):
                        if board[row+drow][col+dcol] == ".":
                            for number in numbers:
                                if checkV(number, col+dcol) and checkH(number, row+drow):
                                    possible[row+drow][col+dcol].append(number)

        for row, col_val in enumerate(possible):
            for col, val in enumerate(col_val):
                if len(val) == 1:
                    board[row][col] = val[0]


        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for possibility in possible[row][col]:
                            if checkV(possibility, col) and checkH(possibility, row) and checkS(possibility, row, col):
                                board[row][col] = possibility
                                if solve():
                                    return True
                                else:
                                    board[row][col] = "."
                        return False
            return True
                
        solve()
        print(board)

sol = Solution()
mat = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(sol.solveSudoku(mat))