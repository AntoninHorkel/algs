import numpy as np

if __name__ == "__main__":
    maze = np.array([
        [True, False, False, False],
        [True, True, False, True],
        [False, True, False, False],
        [True, True, True, True],
    ], dtype=np.bool_)

    def step(maze: np.ndarray, coords: tuple[int, int]) -> bool:
        print(f"Visited coordanites: {coords}")
        if np.all(coords == np.subtract(maze.shape, (1, 1))):
            return True
        maze[coords] = False
        for d_coords in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            try:
                if maze[tuple(np.add(coords, d_coords))]:
                    return step(maze, tuple(np.add(coords, d_coords)))
            except:
                continue
        return False

    print("Wall: █")
    print("Path: ░")

    for y in range(maze.shape[0]):
        for x in range(maze.shape[1]):
            print("░░" if maze[y, x] else "██", end="")
        print()

    print(f"Maze is{"" if step(maze, (0, 0)) else "n't"} solvable.")
