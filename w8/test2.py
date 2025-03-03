class Distances:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def find_distances(self, start_node):
        distances = {}

        queue = [start_node]
        distances[start_node] = 0

        for node in queue:
            distance = distances[node]
            print("distance ", distance, "of node ", node)
            for next_node in self.graph[node]:
                print("before if next_node", next_node,
                      "node", self.graph[node])
                if next_node not in distances:
                    queue.append(next_node)
                    distances[next_node] = distance + 1
                    print("next_node", next_node, "distance",
                          distances[next_node], "queue", queue)

        return distances


d = Distances([1, 2, 3, 4, 5])

d.add_edge(1, 2)
d.add_edge(1, 3)
d.add_edge(1, 4)
d.add_edge(2, 4)
d.add_edge(2, 5)
d.add_edge(3, 4)
d.add_edge(4, 5)

print(d.find_distances(1))  # {1: 0, 2: 1, 3: 1, 4: 1, 5: 2}
