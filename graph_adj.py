# NODES = [0, 1, 2, 3]
# EDGES = [(0, 2), (0, 1), (1, 2), (2, 0), (2, 3), (3, 3)]
NODES = [1, 2, 3, 4, 5, 6, 7]
EDGES = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 4), (2, 5), (3, 1), (3, 4), (3, 7), (4, 2), (4, 3), (4, 6), (4, 1), (5, 2),
         (5, 6), (5, 7), (6, 4), (6, 5), (6, 7), (7, 3), (7, 6), (7, 5)]

from collections import deque


class Graph:
    def __init__(self, nv):
        self.vertices = nv
        self.adj_matrix = [[0] * nv for _ in range(nv)]
        self.visited = [0] * nv

    def add_edge(self, edge_set):
        for src, des in edge_set:
            if src < self.vertices and des < self.vertices:
                self.adj_matrix[src][des] = 1
                self.adj_matrix[des][src] = 1

    def print_graph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.adj_matrix[i][j], end=' ')
            print()

    def BFT(self, start_node):
        visited = [0] * self.vertices
        q = deque([start_node])
        visited[start_node] = 1
        print('BFT')
        while q:
            item = q.popleft()
            print(item, end=' ')
            for i in range(self.vertices):
                if self.adj_matrix[item][i] == 1 and visited[i] == 0:
                    q.append(i)
                    visited[i] = 1
        print()

    def DFT(self, start_node):
        self.visited[start_node] = 1
        print(start_node, end=' ')
        for i in range(self.vertices):
            if self.adj_matrix[start_node][i] == 1 and self.visited[i] == 0:
                self.DFT(i)


graph = Graph(len(NODES)+1)
graph.add_edge(EDGES)
graph.print_graph()
graph.BFT(1)
graph.DFT(1)
