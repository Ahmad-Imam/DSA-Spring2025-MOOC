def check_year(year):
    # TODO
    first_half = year // 100
    second_half = year % 100

    sum = first_half + second_half

    if (sum*sum) == year:
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_year(1995))  # False
    print(check_year(2024))  # False
    print(check_year(2025))  # True
    print(check_year(2026))  # False
    print(check_year(3025))  # True
    print(check_year(5555))  # False
