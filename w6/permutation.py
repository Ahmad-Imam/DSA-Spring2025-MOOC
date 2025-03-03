class PermutationTracker:
    def __init__(self):
        # TODO
        self.numberList = set()
        self.maxVal = 0
        self.flag = False

    def append(self, number):
        # TODO
        if number in self.numberList:
            self.flag = True
        self.maxVal = max(number, self.maxVal)
        self.numberList.add(number)

    def check(self):
        # TODO
        if self.flag:
            return False
        else:
            if len(self.numberList) == self.maxVal:
                return True
            else:
                return False


if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check())  # True

    tracker.append(4)
    print(tracker.check())  # False

    tracker.append(2)
    print(tracker.check())  # False

    tracker.append(3)
    print(tracker.check())  # True

    tracker.append(2)
    print(tracker.check())  # False

    tracker.append(5)
    print(tracker.check())  # False

    tracker = PermutationTracker()
    total = 0
    for i in range(10**5):
        if i % 2 == 0:
            tracker.append(i + 2)
        else:
            tracker.append(i)
        if tracker.check():
            total += 1
    print(total)  # 50000
