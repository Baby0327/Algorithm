n = int(input())
a = list(map(int, input().split()))
odd = len([a[i] for i in range(n) if a[i] % 2])
print(1 if (n + 1) // 2 == odd else 0)