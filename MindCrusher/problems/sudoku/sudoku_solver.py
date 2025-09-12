SYMBOLS_16 = [str(i) for i in range(1, 10)] + [chr(ord('A')+i) for i in range(7)]


class SudokuSolver:
    """Solver Sudoku 9x9."""

    SIZE = 9
    BLOCK = 3

    def __init__(self, grid):
        self.grid = grid

    def find_empty(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def is_safe(self, row, col, num):
        if num in self.grid[row]:
            return False
        for i in range(self.SIZE):
            if self.grid[i][col] == num:
                return False
        start_row = row - row % self.BLOCK
        start_col = col - col % self.BLOCK
        for i in range(self.BLOCK):
            for j in range(self.BLOCK):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_step(self, gui=None, delay=0.05):
        import time
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if gui:
                    gui.update_cell(row, col, num, "lightgreen")
                    gui.master.update()
                    time.sleep(delay)
                if self.solve_step(gui, delay):
                    return True
                self.grid[row][col] = 0
                if gui:
                    gui.update_cell(row, col, "", "lightcoral")
                    gui.master.update()
                    time.sleep(delay)
        return False


class SudokuSolver16:
    """Solver Sudoku 16x16."""

    SIZE = 16
    BLOCK = 4

    def __init__(self, grid):
        self.grid = grid

    def find_empty(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.grid[i][j] == '':
                    return i, j
        return None

    def is_safe(self, row, col, num):
        if num in self.grid[row]:
            return False
        for i in range(self.SIZE):
            if self.grid[i][col] == num:
                return False
        start_row = row - row % self.BLOCK
        start_col = col - col % self.BLOCK
        for i in range(self.BLOCK):
            for j in range(self.BLOCK):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_step(self, gui=None, delay=0.05):
        import time
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty
        for num in SYMBOLS_16:
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if gui:
                    gui.update_cell(row, col, num, "lightgreen")
                    gui.master.update()
                    time.sleep(delay)
                if self.solve_step(gui, delay):
                    return True
                self.grid[row][col] = ''
                if gui:
                    gui.update_cell(row, col, "", "lightcoral")
                    gui.master.update()
                    time.sleep(delay)
        return False
