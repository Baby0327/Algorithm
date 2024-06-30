N = int(input())

num = list(map(int, input().split()))

tmp = num[0]
result = []
for i in range(N-1):
    if num[i] < num[i+1]:
        if i+1 == N-1:
            result.append(num[-1] - tmp)
    else:
        result.append(num[i]-tmp)
        tmp = num[i+1]

result.sort()
print(result[-1])