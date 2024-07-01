result = [[0 for i in range(5)] for j in range(15)]

for i in range(0,5):
    n = list(input())
    for j in range(0,len(n)):
        result[j][i] = n[j]

for i in range(15):
    for j in range(5):
        if result[i][j] != 0:
            print(result[i][j], end="")