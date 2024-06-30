N, K = map(int, input().split())

result = []

for i in range(1,N+1):
    if N % i == 0:
        result.append(i)

if 0 < len(result) < K:
    print(0)
else:
    print(result[K-1])