import random
from typing import List


class Maze:
    def __init__(self, width: int, height: int):
        if width % 2 == 0:
            width += 1
        if height % 2 == 0:
            height += 1
        self.width = width
        self.height = height
        self.grid = self.generate_maze()

    def generate_maze(self) -> List[List[int]]:
        maze = [[1] * self.width for _ in range(self.height)]
        stack = [(1, 1)]
        maze[1][1] = 0
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        while stack:
            x, y = stack[-1]
            random.shuffle(directions)
            moved = False
            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 <= nx < self.width and 0 <= ny < self.height and maze[ny][nx] == 1:
                    maze[y + dy][x + dx] = 0
                    maze[ny][nx] = 0
                    stack.append((nx, ny))
                    moved = True
                    break
            if not moved:
                stack.pop()
        return maze
