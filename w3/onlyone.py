def find_number(numbers):
    # TODO

    extra_list = [0] * (max(numbers)+1)

    for i in range(0, len(numbers)):
        # print(i)
        extra_list[numbers[i]] += 1

    for i in range(0, len(extra_list)):
        if extra_list[i] == 1:
            return i


if __name__ == "__main__":
    print(find_number([1, 1, 1, 2]))  # 2
    print(find_number([1, 5, 5]))  # 2

    print(find_number([1, 1, 2, 1]))  # 2
    print(find_number([1, 2, 1, 1]))  # 2
    print(find_number([2, 1, 1, 1]))  # 2
    print(find_number([5, 5, 5, 3, 5]))  # 3
    print(find_number([1, 100, 1]))  # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers))  # 2
