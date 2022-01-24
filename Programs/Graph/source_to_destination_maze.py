from collections import deque

ROW = 9
COL = 10


def is_valid_cell(x, y):
    if 0 <= x < ROW and 0 <= y < COL:
        return True
    return False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class dequeNode:
    def __init__(self, pt: Point, dis):
        self.node = pt
        self.distance = dis


def bfs(matrix, start_point: Point, destination_point: Point):
    if matrix[destination_point.x][destination_point.y] == 0 or matrix[start_point.x][start_point.y] == 0:
        return -1
    row_direction = [-1, 0, 0, 1]
    col_direction = [0, -1, 1, 0]
    visited = [[False for i in range(COL)] for j in range(ROW)]
    visited[start_point.x][start_point.y] = True
    q = deque()
    q_node = dequeNode(start_point, 0)
    q.append(q_node)
    while q:
        current_item = q.popleft()
        points = current_item.node
        if points.x == destination_point.x and points.y == destination_point.y:
            return current_item.distance
        else:
            for i in range(4):
                new_cell_x = points.x + row_direction[i]
                new_cell_y = points.y + col_direction[i]
                if is_valid_cell(new_cell_x, new_cell_y) and not visited[new_cell_x][new_cell_y] and matrix[new_cell_x][
                    new_cell_y] == 1:
                    visited[new_cell_x][new_cell_y] = True
                    new_q_node = dequeNode(Point(new_cell_x, new_cell_y), current_item.distance + 1)
                    q.append(new_q_node)
    return -1


MATRIX = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
          [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
          [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
          [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]
source = Point(0, 0)
destination = Point(3, 4)

distance = bfs(MATRIX, source, destination)

if distance != -1:
    print("Shortest Path is", distance)
else:
    print("Shortest Path doesn't exist")
