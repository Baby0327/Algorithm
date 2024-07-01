N = int(input())

num = list(input())

result = 0
i = 0

for x in range(N):
    result += int(num[i])
    i += 1

print(result)