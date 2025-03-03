class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"


def find_levels(node):
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
    answerList = []
    for key in sorted(answerDict.keys()):
        answerList.append(sorted(answerDict[key]))
    return answerList


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_levels(tree1))  # [[1], [2, 4, 5], [3, 6, 7]]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_levels(tree2))  # [[1], [2], [3], [4]]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_levels(tree3))  # [[1], [2, 3, 4]]
