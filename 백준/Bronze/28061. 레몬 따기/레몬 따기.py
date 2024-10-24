n = int(input())
lemon = list(map(int, input().split()))
print(max(lemon[i] - (n - i) for i in range(n)))