
class Components:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}
        self.counter = 0
        self.components = {}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def visit(self, node):
        if node in self.components:
            return
        self.components[node] = self.counter
        for node in self.graph[node]:
            self.visit(node)

    def find_components(self):
        for node in self.nodes:
            if node not in self.components:
                self.counter += 1
                self.visit(node)

        return self.counter


def connected(nodes, edges):
    # TODO
    c = Components(nodes)
    for edge in edges:
        c.add_edge(edge[0], edge[1])

    answer = c.find_components()

    return answer == 1


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(nodes, edges))  # True

    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(connected(nodes, edges))  # False

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(connected(nodes, edges))  # False

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(connected(nodes, edges))  # True
