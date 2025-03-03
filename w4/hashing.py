def hash_value(string):
    sum = 0
    A = 23
    M = pow(2, 32)

    for i in range(0, len(string)):
        power = len(string) - i - 1
        charValue = ord(string[i]) - ord("a")
        # print(charValue)
        sum = sum+charValue * pow(A, power)

    return sum % M


if __name__ == "__main__":
    print(hash_value("abc"))  # 25
    print(hash_value("kissa"))  # 2905682
    print(hash_value("aybabtu"))  # 154753059
    print(hash_value("tira"))  # 235796
    print(hash_value("zzzzzzzzzz"))  # 2739360440
