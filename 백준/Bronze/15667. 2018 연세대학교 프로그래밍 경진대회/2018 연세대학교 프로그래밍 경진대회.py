n = int(input()) - 1

for i in range(1, 101):
    if i * (i + 1) == n:
        print(i)
        break