n = int(input())
t = sorted(list(map(int, input().split())))
d = sorted([t[i] - i for i in range(n)])
print(n + 1 if d[-1] <= 0 else n + 1 + d[-1])