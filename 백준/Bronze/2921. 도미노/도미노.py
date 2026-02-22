n = int(input())
print(sum([int(i * (i + 1) * 1.5) for i in range(1, n + 1)]))