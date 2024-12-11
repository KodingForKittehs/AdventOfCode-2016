# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring
import numpy as np


def file_as_line(file):
    with open(file, encoding="utf-8") as f:
        return f.readline().strip()


dirs_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)] # E S W N

def solve():
    facing = 3
    pos = np.array([0, 0])
    visited = set()
    p2 = 0
    for d in  file_as_line("input").split(", "):
        match (d[0], int(d[1:])):
            case "L", steps:
                facing = (facing - 1 ) % 4
            case "R", steps:
                facing = (facing + 1 ) % 4
        for _ in range(0, steps):
            pos += np.array(dirs_4[facing])
            if tuple(pos) in visited:
                if p2 == 0:
                    p2 = abs(pos[0]) + abs(pos[1])
            visited.add(tuple(pos))

    print(f"P1 {abs(pos[0]) + abs(pos[1])}")
    print(f"P2 {p2}")

solve()
