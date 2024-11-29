n = sorted(list(map(int, input().split())))
print(sum(n[2] - n[i] for i in range(3)))