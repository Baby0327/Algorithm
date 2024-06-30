N, K = map(int, input().split())
temp = list(map(int, input().split()))

result = [sum(temp[:K])]
for i in range(N-K):
    result.append(result[-1]-temp[i]+temp[i+K])

print(max(result))