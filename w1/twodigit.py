

def count_numbers(a, b):
    # TODO
    count = 0
    digits = {"0", "1", "3", "4", "6", "7", "8", "9"}
    for i in range(a, b+1):
        for d in digits:
            if d in str(i):
                break
        else:
            count += 1
    return count


if __name__ == "__main__":
    print(count_numbers(1, 10**9))  # 1022
    print(count_numbers(1, 100))  # 6
    print(count_numbers(60, 70))  # 0
    print(count_numbers(25, 25))  # 1

    print(count_numbers(123456789, 987654321))  # 512
