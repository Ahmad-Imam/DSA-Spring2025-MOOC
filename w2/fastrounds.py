def count_rounds(numbers):
    # TODO
    positions = [0] * (len(numbers)+1)

    for i in range(len(numbers)):
        positions[numbers[i]] = i

    rounds = []

    small_round = [1]

    for i in range(2, len(numbers)+1):
        if positions[i] > positions[i-1]:
            small_round.append(i)
        else:
            rounds.append(small_round)
            small_round = [i]
    rounds.append(small_round)

    return len(rounds)


if __name__ == "__main__":
    # print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    # print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]

    # print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]

    # print(find_rounds([1]))
    # [[1]]

    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
