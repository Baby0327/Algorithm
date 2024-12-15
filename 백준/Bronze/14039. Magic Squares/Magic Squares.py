num = [list(map(int, input().split())) for _ in range(4)]
result = []

for i in range(4):
    result.append(sum(num[i]))
    result.append(sum([num[j][i] for j in range(4)]))

print("magic" if result.count(result[0]) == 8 else "not magic")