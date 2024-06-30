a, p = map(int, input().split())
result = [a]

while True:
    tmp = 0
    for i in str(result[-1]):
        tmp += int(i)**p
    if tmp in result:
        result = result[:result.index(tmp)]
        break
    else:
        result.append(tmp)

print(len(result))