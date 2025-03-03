class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"


def count_nodes(node, depth):
    # TODO

    def traverse(node, depth, answerDict=None):
        if answerDict is None:
            answerDict = {}
        if depth not in answerDict:
            answerDict[depth] = []
        answerDict[depth].append(node.value)
        for child in node.children:
            traverse(child, depth + 1, answerDict)
        return answerDict

    answerDict = traverse(node, 0)
    if depth in answerDict:
        return len(answerDict[depth])
    else:
        return 0


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    # print(traverse(tree1, 0))

    print(count_nodes(tree1, 0))  # 1
    print(count_nodes(tree1, 1))  # 3
    print(count_nodes(tree1, 2))  # 3
    print(count_nodes(tree1, 3))  # 0

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_nodes(tree2, 0))  # 1
    print(count_nodes(tree2, 1))  # 1
    print(count_nodes(tree2, 2))  # 1
    print(count_nodes(tree2, 3))  # 1
    print(count_nodes(tree2, 4))  # 0

    # tree3 = Node(1, [Node(2), Node(3), Node(4)])
    # print(count_nodes(tree3, 0))  # 1
    # print(count_nodes(tree3, 1))  # 3
    # print(count_nodes(tree3, 2))  # 0
