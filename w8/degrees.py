class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)


def find_degrees(nodes, edges):
    g = Graph(nodes)
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    degrees = []
    for node in nodes:
        degrees.append(len(g.graph[node]))

    return sorted(degrees)


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(find_degrees(nodes, edges))  # [2, 2, 3, 3, 4]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_degrees(nodes, edges))  # [0, 0, 0, 0, 0]
