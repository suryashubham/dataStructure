# NODES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# # EDGES = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('C', 'E'), ('C', 'F'),
# #          ('B', 'E'), ('E', 'G'), ('F', 'G'), ('D', 'F')]
# EDGES = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'F'), ('A', 'G'), ('F', 'G')]
NODES = [1, 2, 3, 4, 5, 6, 7]
EDGES = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 4), (2, 5), (3, 1), (3, 4), (3, 7), (4, 2), (4, 3), (4, 6), (4, 1), (5, 2),
         (5, 6), (5, 7), (6, 4), (6, 5), (6, 7), (7, 3), (7, 6), (7, 5)]

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
        self.q = deque([])
        self.distance = {}
        self.new_adj = {}

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
            self.new_adj[ele] = []
            print(ele, end='')
            visited[ele] = 1
            neighbours = self.adj_list[ele]
            for item in neighbours:
                if visited[item] == 0 and item not in q:
                    self.new_adj[ele].append(item)
                    q.append(item)
        print()

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

    def sssp(self, start_node, destination_node):
        self.q.append(start_node)
        self.distance[start_node] = 0
        q = self.q
        while q:
            item = q.popleft()
            self.visited[item] = 1
            for element in self.new_adj[item]:
                if self.visited[element] == 0:
                    q.append(element)
                    self.distance[element] = self.distance[item] + 1
        print("shortest distance between {} and {} nodes is {}".format(start_node, destination_node,
                                                                       self.distance[destination_node]))


demo = Graph(NODES, EDGES)
# print(demo.adj_list)
demo.bft(1)
# print(demo.new_adj)
# demo.dft("A")
# print((demo.detect_cycle(0, "-1")))
demo.sssp(1, 7)
