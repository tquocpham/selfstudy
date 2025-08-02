class Solution(object):
    BOARD_SIZE = 9
    GRID_SIZE = 3

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        is_complete = self.is_complete(board)
        last_board = self.copy(board)
        while not is_complete:
            for row in range(Solution.BOARD_SIZE):
                row_vals = self.get_row(row, board)
                poss_row_vals = self.missing_values(row_vals)
                for col in range(Solution.BOARD_SIZE):
                    if board[row][col] != '.':
                        continue
                    square_cell_vals = self.get_square_cell(row, col, board)
                    # print(row, col, square_cell_vals)
                    poss_square_cell_vals = self.missing_values(
                        square_cell_vals)
                    col_vals = self.get_col(col, board)
                    poss_col_vals = self.missing_values(col_vals)
                    possible_vals = self.get_possible_values(
                        poss_square_cell_vals, poss_col_vals, poss_row_vals)
                    # print(row, col, square_cell_vals, row_vals, col_vals)
                    print(poss_square_cell_vals, poss_col_vals,
                          poss_row_vals, possible_vals)
                    if len(possible_vals) == 1:
                        print(f'setting {row} {col}={possible_vals}')
                        board[row][col] = str(possible_vals[0])

            # no change was detected from last board to this one, this means that this board cannot be solved.
            if self.compare(last_board, board):
                break
            last_board = self.copy(board)
            is_complete = self.is_complete(board)
        for row in range(Solution.BOARD_SIZE):
            print(board[row])

    def compare(self, b1, b2):
        for row in range(Solution.BOARD_SIZE):
            for col in range(Solution.BOARD_SIZE):
                if b1[row][col] != b2[row][col]:
                    return False
        return True

    def copy(self, board):
        cpy = []
        for row in range(Solution.BOARD_SIZE):
            cpy_row = []
            for col in range(Solution.BOARD_SIZE):
                v = board[row][col]
                cpy_row.append(v)
            cpy.append(cpy_row)
        return cpy

    def get_possible_values(self, square_values, col_values, row_values):
        possible_values = []
        for v in square_values:
            if v in col_values and v in row_values:
                possible_values.append(v)
        return possible_values

    def missing_values(self, values):
        missing_values = []
        for i in range(1, Solution.BOARD_SIZE+1):
            if not str(i) in values:
                missing_values.append(i)
        return missing_values

    def is_complete(self, board):
        '''
        returns if the board has any empty spots
        '''
        for r in range(Solution.BOARD_SIZE):
            for c in range(Solution.BOARD_SIZE):
                v = board[r][c]
                if v == ".":
                    return False
        return True

    def get_square_cell(self, row, col, board):
        '''
        returns the 3x3 grid that contains row and col;
        for example if 2, 2, return all values for square cell 1
        '''
        grid_row = int(row/Solution.GRID_SIZE)
        grid_col = int(col/Solution.GRID_SIZE)

        row_min = Solution.GRID_SIZE*grid_row
        cols_min = Solution.GRID_SIZE*grid_col

        rows_max = (Solution.GRID_SIZE*(grid_row+1))
        cols_max = (Solution.GRID_SIZE*(grid_col+1))

        values = []
        for r in range(row_min, rows_max):
            for c in range(cols_min, cols_max):
                values.append(board[r][c])
        print(row, col, values)
        return values

    def get_row(self, row_number, board):
        '''
        returns the 3x3 grid
        '''
        return board[row_number]

    def get_col(self, col_number, board):
        '''
        returns the 3x3 grid
        '''

        return [board[r][col_number] for r in range(Solution.BOARD_SIZE)]


sln = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
sln.solveSudoku(board)
