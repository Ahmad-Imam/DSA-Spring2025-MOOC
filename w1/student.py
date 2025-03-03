import math


def check_number(number):
    if number[0] != "0":
        return False
    if len(number) != 9:
        return False
    # TODO
    modified_number = number[0:len(number)-1]
    # print(modified_number)
    checkers = [3, 7, 1, 3, 7, 1, 3, 7]
    sum = 0
    for i in range(len(modified_number)):
        sum += int(modified_number[i]) * checkers[i]
    # print(sum)
    check_digit = (10 - (sum % 10)) % 10
    # print(check_digit)
    if check_digit == int(number[len(number)-1]):
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_number("059103335"))  # False
    '''
    print(check_number("012749139"))  # True
    print(check_number("013333337"))  # True
    print(check_number("012345678"))  # False
    print(check_number("012344550"))  # True
    print(check_number("1337"))  # False
    print(check_number("0127491390"))  # False
    '''
