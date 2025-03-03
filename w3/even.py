def count_sublists(numbers):
    # TODO
    big = []
    small = []
    cnt = 0
    for i in range(0, len(numbers)):

        if numbers[i] % 2 == 0:
            small.append(numbers[i])
        else:
            if len(small) > 0:
                big.append(small)
            small = []

    if len(small) > 0:
        big.append(small)
    print(big)
    for i in range(0, len(big)):
        cnt += len(big[i])*(len(big[i])+1)//2
    return cnt


if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6]))  # 4
    # print(count_sublists([1, 2, 3, 4]))  # 2
    # print(count_sublists([1, 1, 1, 1]))  # 0
    # print(count_sublists([2, 2, 2, 2]))  # 10
    # print(count_sublists([1, 1, 2, 1]))  # 1

    # numbers = [2] * 10**5
    # print(count_sublists(numbers))  # 5000050000
