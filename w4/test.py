import time


def count_rounds_dict(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds


def count_rounds(numbers):
    # TODO
    positions = [0] * (len(numbers)+1)

    for i in range(len(numbers)):
        positions[numbers[i]] = i

    rounds = []

    small_round = [1]

    for i in range(2, len(numbers)+1):
        if positions[i] > positions[i-1]:
            small_round.append(i)
        else:
            rounds.append(small_round)
            small_round = [i]
    rounds.append(small_round)


n = 10**7


start_time = time.time()
numbers = list(reversed(range(1, n+1)))
print(count_rounds_dict(numbers))  # 100000
end_add = time.time()

start_time = time.time()
numbers = list(reversed(range(1, n+1)))
print(count_rounds(numbers))  # 100000
end_del = time.time()

print("Dict time:", round(end_add - start_time, 2), "s")
print("List time:", round(end_del - end_add, 2), "s")
