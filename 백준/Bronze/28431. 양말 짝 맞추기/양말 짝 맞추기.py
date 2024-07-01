result = []

for _ in range(5):
    n = int(input())
    if n in result:
        result.remove(n)
    else:
        result.append(n)

print(result[0])