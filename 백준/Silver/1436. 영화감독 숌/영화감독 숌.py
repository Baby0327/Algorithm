N = int(input())

result = [666]
i = 1666
while len(result) < N:
    if "666" in str(i):
        result.append(i)
    i += 1

print(result[-1])