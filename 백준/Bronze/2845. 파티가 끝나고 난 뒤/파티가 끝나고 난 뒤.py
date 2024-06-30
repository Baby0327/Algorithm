L, P = map(int, input().split())

num = list(map(int, input().split()))

result = []

for i in num:
    result.append(i-L*P)

for i in result:
    print(i, end=" ")