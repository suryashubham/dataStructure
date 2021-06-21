NODES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
EDGES = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('C', 'E'), ('C', 'F'),
         ('B', 'E'), ('E', 'G'), ('F', 'G'), ('D', 'F')]

from collections import deque


class Graph:
    def __init__(self, nodes, edges, DIRECTED=False):
        self.nodes = nodes
        self.edges = edges
        self.adj_list = {}
        self.is_directed = DIRECTED
        self.create_default_adj_list()
        self.construct_graph()

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


demo = Graph(NODES, EDGES)
demo.bft("C")
