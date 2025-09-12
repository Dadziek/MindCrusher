import tkinter as tk
from problems.sudoku.sudoku_gui import run_sudoku
from problems.maze.maze_gui import run_maze


def main_menu():
    root = tk.Tk()
    root.title("MindCrusher – wybierz problem")

    tk.Label(root, text="Wybierz problem do wizualizacji:",
             font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="Sudoku", width=20,
              command=lambda: run_sudoku(root)).pack(pady=5)

    tk.Button(root, text="Labirynt", width=20,
              command=lambda: run_maze(root)).pack(pady=5)

    tk.Button(root, text="Zamknij", width=20,
              command=root.destroy).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main_menu()
