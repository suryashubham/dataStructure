# NODES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# # EDGES = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('C', 'E'), ('C', 'F'),
# #          ('B', 'E'), ('E', 'G'), ('F', 'G'), ('D', 'F')]
# EDGES = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'F'), ('A', 'G'), ('F', 'G')]
NODES = [0, 1, 2, 3]
EDGES = [(0, 2), (0, 1), (1, 2), (2, 0), (2, 3), (3, 3)]

from collections import deque


class Graph:
    def __init__(self, nodes, edges, DIRECTED=False):
        self.nodes = nodes
        self.edges = edges
        self.adj_list = {}
        self.is_directed = DIRECTED
        self.create_default_adj_list()
        self.visited = {v: 0 for v in self.adj_list}
        self.construct_graph()
        self.stack = deque([])

    def create_default_adj_list(self):
        vertices = self.nodes
        for vertex in vertices:
            self.adj_list[vertex] = []

    def construct_graph(self):
        for source, destination in self.edges:
            self.adj_list[source].append(destination)
            if not self.is_directed:
                self.adj_list[destination].append(source)

    def bft(self, start_node):
        visited = {v: 0 for v in self.adj_list}
        q = deque([])
        q.append(start_node)
        print('Breadth First Traversal:', end=' ')
        while q:
            ele = q.popleft()
            print(ele + " ", end='')
            visited[ele] = 1
            neighbours = self.adj_list[ele]
            for item in neighbours:
                if visited[item] == 0 and item not in q:
                    q.append(item)

    def dft(self, start_node):
        # visited = {v: 0 for v in self.adj_list}
        self.visited[start_node] = 1
        print(start_node)
        for w in self.adj_list[start_node]:
            if self.visited[w] == 0:
                self.dft(w)

    def detect_cycle(self, start_node, parent_node):
        if self.visited[start_node] == 0:
            self.visited[start_node] = 1
        for w in self.adj_list[start_node]:
            if self.visited[w] == 0:
                return self.detect_cycle(w, start_node)
            elif self.visited[w] == 1 and parent_node != w:
                return True
        return False


demo = Graph(NODES, EDGES)
# print(demo.adj_list)
# demo.bft("C")
# demo.dft("A")
print((demo.detect_cycle(0, "-1")))
