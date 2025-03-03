class MaxList:
    def __init__(self):
        # TODO
        self.numberList = []
        self.maxCount = 0

    def append(self, number):
        # TODO
        self.numberList.append(number)
        self.maxCount = max(self.maxCount, number)

    def max(self):
        # TODO
        return self.maxCount


if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max())  # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max())  # 8

    numbers = MaxList()
    total = 0
    for i in range(10**5):
        numbers.append(i * 999983 % 10**9)
        total += numbers.max()
    print(total)  # 99498381797517
