n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sum((i + j) * max(i, j) for i in a for j in b))