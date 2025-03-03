def count_pairs(numbers):

    sorted_numbers = sorted(numbers)

    n = len(sorted_numbers)

    left = 0
    right = n // 2
    count = 0

    while left < n // 2 and right < n:
        if sorted_numbers[right] >= 2 * sorted_numbers[left]:
            count += 1
            left += 1
            right += 1
        else:

            right += 1

    return count


if __name__ == "__main__":
    print(count_pairs([1]))  # 0
    print(count_pairs([1, 2, 3]))  # 1
    print(count_pairs([1, 2, 3, 4]))  # 2
    print(count_pairs([1, 1, 1, 1]))  # 0
    print(count_pairs([10**9, 1, 1, 1]))  # 1
    print(count_pairs([4, 5, 1, 4, 7, 8]))  # 2
    print(count_pairs([1, 2, 3, 2, 4, 6]))  # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers))  # 41176
