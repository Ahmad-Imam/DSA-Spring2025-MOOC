class Components:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}
        self.visited = set()
        self.big = []
        self.small = []

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def visit(self, node):
        if node in self.visited:
            return
        self.visited.add(node)
        self.small.append(node)
        for node in self.graph[node]:
            self.visit(node)

    def find_components(self):
        for node in self.nodes:
            if node not in self.visited:
                self.visit(node)
                self.big.append(sorted(self.small))
                self.small = []
        return self.big


def find_components(nodes, edges):
    # TODO
    c = Components(nodes)
    for edge in edges:
        c.add_edge(edge[0], edge[1])

    components = c.find_components()
    return components


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges))  # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges))  # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges))  # [[1, 2, 3, 4, 5]]
