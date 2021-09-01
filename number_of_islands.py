from collections import deque

data = [[1, 1, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

ROW = len(data)
COL = len(data[0])

islands = 0

visited = [[False for _ in range(len(data[0]))] for _ in range(len(data))]

direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]


def get_total_number_of_island():
    global islands
    for i in range(ROW):
        for j in range(COL):
            if data[i][j] == 1 and not visited[i][j] and is_valid(i, j):
                visited[i][j] = True
                islands += 1
                mark_neighbouring_islands(i, j)


def mark_neighbouring_islands(x, y):
    for k in range(len(direction)):
        new_x = x + direction[k][0]
        new_y = y + direction[k][1]
        if is_valid(new_x, new_y) and data[new_x][new_y] == 1 and not visited[new_x][new_y]:
            visited[new_x][new_y] = True
            mark_neighbouring_islands(new_x, new_y)


def is_valid(row, col):
    return 0 <= row < ROW and 0 <= col < COL


get_total_number_of_island()
print(islands)
