class RepeatList:
    def __init__(self):
        # TODO
        self.numberList = {}
        self.flag = False

    def append(self, number):
        # TODO
        if number not in self.numberList:
            self.numberList[number] = 1
        else:
            self.flag = True

    def repeat(self):
        # TODO
        return self.flag


if __name__ == "__main__":
    numbers = RepeatList()

    print(numbers.repeat())  # False

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.repeat())  # False

    numbers.append(2)
    print(numbers.repeat())  # True

    numbers.append(5)
    print(numbers.repeat())  # True

    numbers = RepeatList()
    total = 0
    for i in range(10**5):
        numbers.append(i * 999983 % 12345)
        if numbers.repeat():
            total += 1
    print(total)  # 87655
