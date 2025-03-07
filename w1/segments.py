def find_segments(data):
    # TODO
    segments = []
    if len(data) == 0:
        return segments
    current = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current:
            count += 1
        else:
            segments.append((count, current))
            current = data[i]
            count = 1
    segments.append((count, current))
    return segments


if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]

    print(find_segments("mmzxzj"))
