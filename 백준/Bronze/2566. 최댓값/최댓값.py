num = []

for i in range(9):
    n = list(map(int, input().split()))
    num.append(n)

result = 0

for i in num:
    for j in i:
        if result < j:
            result = j

print(result)

for i in range(9):
    for j in range(9):
        if num[i][j] == result:
            print(i+1, j+1)