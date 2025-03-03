class SumList:
    def __init__(self):
        # TODO

        self.sumDict = {}
        self.i = 0

    def append(self, number):
        # TODO
        if self.i == 0:
            self.sumDict[self.i] = number
            self.i += 1
        else:
            self.sumDict[self.i] = self.sumDict[self.i-1] + number
            self.i += 1

    def sum(self, a, b):
        # TODO

        if a != 0:
            answer = self.sumDict[b] - self.sumDict[a-1]
        else:
            answer = self.sumDict[b]
        return answer


if __name__ == "__main__":
    numbers = SumList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    numbers.append(4)
    numbers.append(5)

    print(numbers.sum(0, 4))  # 15
    print(numbers.sum(1, 1))  # 2
    print(numbers.sum(1, 3))  # 9
    print(numbers.sum(2, 3))  # 7
    print(numbers.sum(0, 3))  # 10

    numbers.append(1)
    print(numbers.sum(0, 5))  # 16
    print(numbers.sum(5, 5))  # 1

    numbers = SumList()
    total = 0
    for i in range(10**5):
        numbers.append(i + 1)
        total += numbers.sum(i // 2, i)
    print(total)  # 125005000050000
