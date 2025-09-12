import tkinter as tk
from tkinter import ttk
from .sudoku_generator import SudokuGenerator, SudokuGenerator16
from .sudoku_solver import SudokuSolver, SudokuSolver16
from .sudoku_gui_class import SudokuGUI  # tu trzymasz klasę SudokuGUI


def run_sudoku(parent_root=None):
    window = tk.Toplevel(parent_root) if parent_root else tk.Tk()
    window.title("Sudoku Solver - wizualizacja")

    size_var = tk.StringVar(value="9x9")
    ttk.Label(window, text="Wybierz rozmiar planszy:").grid(row=0, column=0, columnspan=2)
    size_combo = ttk.Combobox(window, textvariable=size_var,
                              values=["9x9", "16x16"], state="readonly")
    size_combo.grid(row=0, column=2, columnspan=2)

    gui_instance = {}

    def start_app():
        for widget in window.winfo_children()[1:]:
            widget.destroy()
        size = size_var.get()
        if size == "9x9":
            gui_instance["gui"] = SudokuGUI(window, SudokuGenerator, SudokuSolver, default_k=30)
        else:
            gui_instance["gui"] = SudokuGUI(window, SudokuGenerator16, SudokuSolver16, default_k=80)

    start_btn = tk.Button(window, text="Start", command=start_app)
    start_btn.grid(row=0, column=4, columnspan=2)

    window.mainloop()
