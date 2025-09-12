import tkinter as tk


class MazeVisualizer:
    def __init__(self, canvas: tk.Canvas, maze, cell_size=20):
        self.canvas = canvas
        self.maze = maze
        self.cell_size = cell_size
        self.visited_color = "lightblue"
        self.path_color = "yellow"

    def calculate_cell_size(self):
        cw = self.canvas.winfo_width() // self.maze.width
        ch = self.canvas.winfo_height() // self.maze.height
        self.cell_size = max(1, min(cw, ch))

    def draw_maze(self, visited=None, path=None):
        if path is None:
            path = []
        if visited is None:
            visited = []
        self.canvas.delete("all")
        self.calculate_cell_size()
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                x1 = x * self.cell_size
                y1 = y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = "black" if self.maze.grid[y][x] == 1 else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="lightgray")

        # odwiedzone
        for x, y in visited:
            x1, y1 = x * self.cell_size, y * self.cell_size
            x2, y2 = x1 + self.cell_size, y1 + self.cell_size
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.visited_color, outline="lightgray")

        # ścieżka
        for x, y in path:
            x1, y1 = x * self.cell_size, y * self.cell_size
            x2, y2 = x1 + self.cell_size, y1 + self.cell_size
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.path_color, outline="lightgray")

        # start/meta
        sx, sy = 1, 1
        gx, gy = self.maze.width - 2, self.maze.height - 2
        self.canvas.create_rectangle(sx * self.cell_size, sy * self.cell_size,
                                     (sx + 1) * self.cell_size, (sy + 1) * self.cell_size,
                                     fill="green", outline="lightgray")
        self.canvas.create_rectangle(gx * self.cell_size, gy * self.cell_size,
                                     (gx + 1) * self.cell_size, (gy + 1) * self.cell_size,
                                     fill="red", outline="lightgray")
        self.canvas.update()
