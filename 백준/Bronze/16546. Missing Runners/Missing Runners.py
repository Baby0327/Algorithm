n = int(input())
num = set(list(map(int, input().split())))
print(*list(set(i for i in range(1, n + 1)) - num))