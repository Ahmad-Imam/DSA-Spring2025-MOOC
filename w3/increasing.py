def count_sublists(numbers):
    # TODO
    big = []
    small = []
    cnt = 0
    small.append(numbers[0])
    for i in range(1, len(numbers)):

        if numbers[i] > numbers[i-1]:
            small.append(numbers[i])

        else:
            big.append(small)
            small = []
            small.append(numbers[i])

    if len(small) > 0:
        big.append(small)

    for i in range(0, len(big)):
        cnt += len(big[i])*(len(big[i])+1)//2
    return cnt


if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4]))  # 7
    print(count_sublists([1, 2, 3, 4]))  # 10
    print(count_sublists([4, 3, 2, 1]))  # 4
    print(count_sublists([1, 1, 1, 1]))  # 4
    print(count_sublists([1, 2, 1, 2]))  # 6

    numbers = list(range(1, 10**5+1))
    print(count_sublists(numbers))  # 5000050000
