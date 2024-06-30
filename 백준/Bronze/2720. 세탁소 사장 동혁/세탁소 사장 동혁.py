T = int(input())
result = [[0 for i in range(4)] for i in range(T)]

for i in range(T):
    n = int(input())
    tmp = 0
    if n >= 25:
        result[i][0] = n//25
        n = n%25
    if n >= 10:
        result[i][1] = n//10
        n = n%10
    if n >= 5:
        result[i][2] = n//5
        n = n%5
    if n < 5:
        result[i][3] = n

for i in result:
    for j in i:
        print(j, end=" ")
    print()