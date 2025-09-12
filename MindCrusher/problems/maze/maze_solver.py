class MazeSolver:
    def __init__(self, maze, visualizer, delay=50):
        self.maze = maze
        self.visualizer = visualizer
        self.delay = delay
        self.stack = [(1, 1)]
        self.visited = set()
        self.path = []

    def step(self):
        if not self.stack:
            # koniec
            self.visualizer.draw_maze(list(self.visited), self.path)
            return

        x, y = self.stack.pop()
        if (x, y) in self.visited:
            self.visualizer.canvas.after(self.delay, self.step)
            return

        self.visited.add((x, y))
        self.path.append((x, y))
        self.visualizer.draw_maze(list(self.visited), self.path)

        if (x, y) == (self.maze.width - 2, self.maze.height - 2):
            self.visualizer.draw_maze(list(self.visited), self.path)
            return

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height:
                if self.maze.grid[ny][nx] == 0 and (nx, ny) not in self.visited:
                    self.stack.append((nx, ny))

        self.visualizer.canvas.after(self.delay, self.step)

    def solve(self):
        self.step()
