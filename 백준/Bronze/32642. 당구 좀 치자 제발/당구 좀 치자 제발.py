n = int(input())
num = list(map(int, input().split()))
result = [1 if num[0] else -1]

for i in range(1, n):
    temp = 1 if num[i] else -1
    result.append(result[-1] + temp)

print(sum(result))