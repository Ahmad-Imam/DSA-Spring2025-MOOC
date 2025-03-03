def count_parts(numbers):

    left = 0

    seen = set()
    count = 0

    for i in range(len(numbers)):
        while numbers[i] in seen:
            seen.remove(numbers[left])
            left += 1
        seen.add(numbers[i])
        count += i-left+1
    return count

    return 1


if __name__ == "__main__":
    print(count_parts([2, 1, 4, 2]))  # 9

    print(count_parts([1, 2, 1, 2]))  # 7
    '''
    print(count_parts([2, 1, 4, 2]))  # 9
    print(count_parts([1, 1, 1, 1]))  # 4
    print(count_parts([1, 2, 3, 4]))  # 10
    print(count_parts([1, 2, 1, 2]))  # 7
    print(count_parts([1, 2, 1, 3]))  # 8
    print(count_parts([1, 1, 2, 1]))  # 6
    '''

    songs = [1, 2] * 10**5
    print(count_parts(songs))  # 399999
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs))  # 15000050000
