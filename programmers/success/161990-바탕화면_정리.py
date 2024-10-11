import numpy as np


def to_np(wallpaper):
    new_wallpaper = []
    for row in wallpaper:
        new_row = []
        for col in row:
            if col == ".":
                new_col = 0
            elif col == "#":
                new_col = 1
            new_row.append(new_col)
        new_wallpaper.append(new_row)
    return np.array(new_wallpaper, dtype=np.uint8)


def solution(wallpaper):
    new_wallpaper = to_np(wallpaper)

    row_indices = np.where(new_wallpaper.any(axis=0))[0]
    col_indices = np.where(new_wallpaper.any(axis=1))[0]
    return (
        int(col_indices[0]),
        int(row_indices[0]),
        int(col_indices[-1] + 1),
        int(row_indices[-1] + 1),
    )


if __name__ == "__main__":
    wallpaper = [".#...", "..#..", "...#."]
    solution(wallpaper)
