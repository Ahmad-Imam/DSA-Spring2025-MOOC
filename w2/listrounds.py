def find_rounds(numbers):
    # TODO

    val = 1
    largeRounds = []
    while val <= len(numbers):
        smallRounds = []
        for i in range(len(numbers)):
            if numbers[i] == val:
                smallRounds.append(val)
                val += 1
        largeRounds.append(smallRounds)

    return largeRounds


if __name__ == "__main__":
    # print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    # print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]

    # print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]

    # print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
