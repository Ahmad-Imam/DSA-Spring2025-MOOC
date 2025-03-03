def find_order(n):

    newList = list(range(1, n + 1))
    remove = False
    answer = []

    while len(newList) > 0:
        currentList = []
        for i in newList:
            if remove:
                answer.append(i)
                remove = False
            else:
                currentList.append(i)
                remove = True
        if remove and len(currentList) > 0:
            answer.append(currentList.pop(0))
            remove = False
        newList = currentList
    return answer


if __name__ == "__main__":
    print(find_order(1))  # [1]
    print(find_order(2))  # [2, 1]
    print(find_order(3))  # [2, 1, 3]
    print(find_order(7))  # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:])  # [52545, 85313, 36161, 3393, 68929]
