x, y, w, h = map(int, input().split())

result = []
result.append(x)
result.append(y)
result.append(w-x)
result.append(h-y)

result.sort()

print(result[0])