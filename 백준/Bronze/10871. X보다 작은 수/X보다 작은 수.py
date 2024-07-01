N, X = map(int, input().split())

num = list(map(int, input().split()))

result = []

for i in num:
    if i < X:
        result.append(i)

for i in result:
    print(i, end=" ")