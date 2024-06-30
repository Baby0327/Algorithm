result = []
tmp = 0
for i in range(4):
    a, b = map(int, input().split())
    result.append(tmp + (b-a))
    tmp = result[i]

print(max(result))