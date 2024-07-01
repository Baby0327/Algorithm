N, X = map(int, input().split())
visit = list(map(int, input().split()))

result = [0 for i in range(N-X+1)]
result[0] = sum(visit[:X])
for i in range(1, N-X+1):
    result[i] = result[i-1] - visit[i-1] + visit[i+X-1]

result.sort()
count = result.count(result[-1])

if result[-1] == 0:
    print("SAD")
else:
    print(result[-1])
    print(count)