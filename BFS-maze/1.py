maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
]


def find_maze_way_out(maze: list[list]) -> list[tuple[int, int]]:
    row_len, col_len = len(maze), len(maze[0])

    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pos_and_path = [[(0, 0), [(0, 0)]]]
    way_out = []

    while True:
        if not pos_and_path:
            break
        pos, path = pos_and_path.pop(0)
        p_x, p_y = pos
        if p_x == row_len - 1 and p_y == col_len - 1:
            way_out.append(path)
            continue
        for x, y in directions:
            p_x += x
            p_y += y
            if (
                0 <= p_x < row_len
                and 0 <= p_y < col_len
                and not visited[p_x][p_y]
                and maze[p_x][p_y] == 0
            ):
                visited[p_x][p_y] = True
                pos_and_path.append([(p_x, p_y), path + [(p_x, p_y)]])

    return way_out


print(find_maze_way_out(maze))
