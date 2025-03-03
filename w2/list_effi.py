import time

n = 10**5
print("n:", n)

lst = []


start_time = time.time()
for i in range(1, n+1):
    lst.append(i)
end_add = time.time()


for _ in range(n):
    lst.pop(0)
end_del = time.time()

print("Addition time:", round(end_add - start_time, 2), "s")
print("Deletion time:", round(end_del - end_add, 2), "s")
