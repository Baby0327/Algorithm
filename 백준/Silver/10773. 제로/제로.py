K = int(input())

result = []

for i in range(K):
    X = int(input())
    if X == 0:
        result.pop(-1)
    else:
        result.append(X)

print(sum(result))