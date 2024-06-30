N, M = map(int,input().split())
num = list(map(int, input().split()))
result = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            test = num[i] + num[j] + num[k]
            if test <= M:
                result.append(test)
            else:
                continue

print(max(result))