import random

# Symboli używamy dla 16x16
SYMBOLS_16 = [str(i) for i in range(1, 10)] + [chr(ord('A') + i) for i in range(7)]


class SudokuGenerator:
    """Generator Sudoku 9x9 z k pustymi polami."""
    SIZE = 9
    BLOCK = 3

    def __init__(self, k):
        self.k = k
        self.grid = [[0] * self.SIZE for _ in range(self.SIZE)]

    def not_used_in_block(self, row_start, col_start, num):
        for i in range(self.BLOCK):
            for j in range(self.BLOCK):
                if self.grid[row_start + i][col_start + j] == num:
                    return False
        return True

    def fill_block(self, row, col):
        for i in range(self.BLOCK):
            for j in range(self.BLOCK):
                while True:
                    num = random.randint(1, 9)
                    if self.not_used_in_block(row, col, num):
                        break
                self.grid[row + i][col + j] = num

    def not_used_in_row(self, i, num):
        return num not in self.grid[i]

    def not_used_in_col(self, j, num):
        for i in range(self.SIZE):
            if self.grid[i][j] == num:
                return False
        return True

    def is_safe(self, i, j, num):
        return (
            self.not_used_in_row(i, num) and
            self.not_used_in_col(j, num) and
            self.not_used_in_block(i - i % self.BLOCK, j - j % self.BLOCK, num)
        )

    def fill_diagonal(self):
        for i in range(0, self.SIZE, self.BLOCK):
            self.fill_block(i, i)

    def fill_remaining(self, i=0, j=0):
        if i == self.SIZE:
            return True
        if j == self.SIZE:
            return self.fill_remaining(i + 1, 0)
        if self.grid[i][j] != 0:
            return self.fill_remaining(i, j + 1)
        for num in range(1, 10):
            if self.is_safe(i, j, num):
                self.grid[i][j] = num
                if self.fill_remaining(i, j + 1):
                    return True
                self.grid[i][j] = 0
        return False

    def remove_k_digits(self):
        k = self.k
        while k > 0:
            cell_id = random.randint(0, self.SIZE**2 - 1)
            i = cell_id // self.SIZE
            j = cell_id % self.SIZE
            if self.grid[i][j] != 0:
                self.grid[i][j] = 0
                k -= 1

    def generate(self):
        self.fill_diagonal()
        self.fill_remaining()
        self.remove_k_digits()
        return self.grid


class SudokuGenerator16:
    """Generator Sudoku 16x16 z k pustymi polami."""
    SIZE = 16
    BLOCK = 4

    def __init__(self, k):
        self.k = k
        self.grid = [[''] * self.SIZE for _ in range(self.SIZE)]

    def not_used_in_block(self, row_start, col_start, num):
        for i in range(self.BLOCK):
            for j in range(self.BLOCK):
                if self.grid[row_start + i][col_start + j] == num:
                    return False
        return True

    def fill_block(self, row, col):
        for i in range(self.BLOCK):
            for j in range(self.BLOCK):
                while True:
                    num = random.choice(SYMBOLS_16)
                    if self.not_used_in_block(row, col, num):
                        break
                self.grid[row + i][col + j] = num

    def not_used_in_row(self, i, num):
        return num not in self.grid[i]

    def not_used_in_col(self, j, num):
        for i in range(self.SIZE):
            if self.grid[i][j] == num:
                return False
        return True

    def is_safe(self, i, j, num):
        return (
            self.not_used_in_row(i, num) and
            self.not_used_in_col(j, num) and
            self.not_used_in_block(i - i % self.BLOCK, j - j % self.BLOCK, num)
        )

    def fill_diagonal(self):
        for i in range(0, self.SIZE, self.BLOCK):
            self.fill_block(i, i)

    def fill_remaining(self, i=0, j=0):
        if i == self.SIZE:
            return True
        if j == self.SIZE:
            return self.fill_remaining(i + 1, 0)
        if self.grid[i][j] != '':
            return self.fill_remaining(i, j + 1)
        for num in SYMBOLS_16:
            if self.is_safe(i, j, num):
                self.grid[i][j] = num
                if self.fill_remaining(i, j + 1):
                    return True
                self.grid[i][j] = ''
        return False

    def remove_k_digits(self):
        k = self.k
        while k > 0:
            cell_id = random.randint(0, self.SIZE**2 - 1)
            i = cell_id // self.SIZE
            j = cell_id % self.SIZE
            if self.grid[i][j] != '':
                self.grid[i][j] = ''
                k -= 1

    def generate(self):
        self.fill_diagonal()
        self.fill_remaining()
        self.remove_k_digits()
        return self.grid
