NODES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
EDGES = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('C', 'E'), ('C', 'F'),
         ('B', 'E'), ('E', 'G'), ('F', 'G'), ('D', 'F')]


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
        print(self.adj_list)


demo = Graph(NODES, EDGES)
