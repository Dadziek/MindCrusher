import tkinter as tk
from .maze_generator import Maze
from .maze_visualizer import MazeVisualizer
from .maze_solver import MazeSolver


class MazeApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(side="left", fill="both", expand=True)

        control_frame = tk.Frame(self, padx=10, pady=10)
        control_frame.pack(side="right", fill="y")

        tk.Label(control_frame, text="Szerokość (kolumny):").pack()
        self.width_entry = tk.Entry(control_frame)
        self.width_entry.insert(0, "21")
        self.width_entry.pack()

        tk.Label(control_frame, text="Wysokość (wiersze):").pack()
        self.height_entry = tk.Entry(control_frame)
        self.height_entry.insert(0, "21")
        self.height_entry.pack()

        tk.Button(control_frame, text="Generuj labirynt", command=self.generate_maze).pack(pady=10)
        tk.Button(control_frame, text="Rozwiąż labirynt", command=self.solve_maze).pack(pady=10)

        self.maze = None
        self.visualizer = None
        self.solver = None

        self.generate_maze()

    def generate_maze(self):
        """Tworzy nowy labirynt i rysuje go"""
        try:
            w = int(self.width_entry.get())
            h = int(self.height_entry.get())
            self.maze = Maze(w, h)
            self.visualizer = MazeVisualizer(self.canvas, self.maze)
            self.visualizer.draw_maze()
            self.solver = MazeSolver(self.maze, self.visualizer)
        except ValueError:
            pass

    def solve_maze(self):
        """Rozpoczyna animowane rozwiązywanie labiryntu"""
        if self.solver:
            self.solver.solve()


# --- uruchomienie aplikacji ---
def run_maze(parent_root=None):
    window = tk.Toplevel(parent_root) if parent_root else tk.Tk()
    window.title("Labirynt – animacja")
    window.geometry("800x600")
    app = MazeApp(window)
    window.mainloop()
