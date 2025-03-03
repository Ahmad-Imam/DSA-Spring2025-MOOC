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
        print("visit node", node, "counter",
              self.counter, "components", self.components)
        if node in self.components:
            return
        self.components[node] = self.counter

        for next_node in self.graph[node]:
            self.visit(next_node)

    def find_components(self):

        for node in self.nodes:
            print("find_comp node", node, "components",
                  self.components, "counter", self.counter)
            if node not in self.components:
                self.counter += 1
                self.visit(node)
        return self.components

    def count_components(self):
        self.find_components()
        return self.counter

    def is_connected(self):
        return self.count_components() == 1


# c = Components([1, 2, 3, 4, 5])

# c.add_edge(1, 2)
# c.add_edge(3, 4)
# c.add_edge(3, 5)
# c.add_edge(4, 5)

# print(c.find_components())  # {1: 1, 2: 1, 3: 2, 4: 2, 5: 2}


edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]


cd = Components([1, 2, 3, 4, 5])

# cd.add_edge(1, 2)
# cd.add_edge(1, 3)
# cd.add_edge(2, 3)
# cd.add_edge(4, 5)
# cd.add_edge(4, 6)
# cd.add_edge(5, 7)
# cd.add_edge(6, 7)
cd.add_edge(1, 2)
cd.add_edge(1, 3)
cd.add_edge(1, 4)
cd.add_edge(2, 4)
cd.add_edge(2, 5)
cd.add_edge(3, 4)
cd.add_edge(4, 5)


print(cd.find_components())
print("Number of connected components:", cd.count_components())
print("Is the graph connected?", cd.is_connected())
