import tkinter as tk
from tkinter import messagebox


class SudokuGUI:
    """GUI do wizualizacji Sudoku (9x9 lub 16x16)."""

    def __init__(self, master, generator_class, solver_class, default_k=None):
        self.master = master
        self.generator_class = generator_class
        self.solver_class = solver_class
        self.cells = []

        # Ustalamy rozmiar planszy i wielkość bloku
        self.SIZE = 9 if generator_class.__name__ == "SudokuGenerator" else 16
        self.BLOCK = 3 if self.SIZE == 9 else 4

        self.create_ui()

        # Generujemy od razu planszę przy starcie
        if default_k is None:
            default_k = 30 if self.SIZE == 9 else 80
        self.k_entry.delete(0, tk.END)
        self.k_entry.insert(0, str(default_k))
        self.generate_new()

    def create_ui(self):
        """Tworzy planszę i kontrolki."""
        self.cells = [[None for _ in range(self.SIZE)] for _ in range(self.SIZE)]

        # Ustawienie wagi wierszy i kolumn
        for i in range(self.SIZE):
            self.master.grid_rowconfigure(i + 1, weight=1)
            self.master.grid_columnconfigure(i, weight=1)
            for j in range(self.SIZE):
                e = tk.Label(
                    self.master,
                    text="",
                    width=4 if self.SIZE == 9 else 3,
                    height=2,
                    borderwidth=1,
                    relief="solid",
                    font=("Arial", 16 if self.SIZE == 9 else 12),
                    bg="white"
                )
                e.grid(row=i + 1, column=j, padx=0, pady=0, sticky="nsew")
                self.cells[i][j] = e

        # Pole do wpisania liczby pustych pól
        tk.Label(self.master, text="Liczba pustych pól:").grid(row=self.SIZE + 1, column=0, columnspan=3)
        self.k_entry = tk.Entry(self.master, width=5)
        self.k_entry.insert(0, "30")
        self.k_entry.grid(row=self.SIZE + 1, column=3, columnspan=1)

        # Przycisk generowania
        generate_btn = tk.Button(
            self.master,
            text="Generuj nowe Sudoku",
            command=self.generate_new
        )
        generate_btn.grid(row=self.SIZE + 1, column=4, columnspan=2, sticky="we")

        # Przycisk rozwiązania
        solve_btn = tk.Button(
            self.master,
            text="Rozwiąż Sudoku",
            command=self.solve_with_visual
        )
        solve_btn.grid(row=self.SIZE + 1, column=6, columnspan=3, sticky="we")

    def generate_new(self):
        """Generuje nową planszę."""
        try:
            k = int(self.k_entry.get())
            if k < 0 or k > self.SIZE ** 2:
                raise ValueError
        except ValueError:
            messagebox.showerror("Błąd", f"Podaj poprawną liczbę pustych pól (0-{self.SIZE ** 2}).")
            return

        self.generator = self.generator_class(k)
        grid = self.generator.generate()
        self.solver = self.solver_class(grid)
        self.update_ui()

    def update_ui(self):
        """Aktualizuje całą planszę."""
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                value = self.generator.grid[i][j]
                self.cells[i][j]["text"] = "" if value in (0, '') else str(value)
                self.cells[i][j]["bg"] = "white"

    def update_cell(self, row, col, value, color):
        """Aktualizuje pojedynczą komórkę."""
        self.cells[row][col]["text"] = "" if value in (0, '') else str(value)
        self.cells[row][col]["bg"] = color

    def solve_with_visual(self):
        """Uruchamia solver i wizualizuje jego działanie."""
        if not self.solver:
            messagebox.showwarning("Uwaga", "Najpierw wygeneruj planszę Sudoku!")
            return
        self.solver.solve_step(gui=self)
