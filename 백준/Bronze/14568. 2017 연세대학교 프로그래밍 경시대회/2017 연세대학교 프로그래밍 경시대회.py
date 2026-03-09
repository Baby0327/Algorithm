n = int(input())
c = 0

for i in range(1, n):
    for j in range(i + 2, n):
        t = n - (i + j)
        if t > 0 and t % 2 == 0:
            c += 1

print(c)