n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(len([1 for i in range(n) for j in range(m) if a[i] <= b[j]]))