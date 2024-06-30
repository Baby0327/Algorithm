T = int(input())
result = []

for x in range(T):
    k = int(input())
    n = int(input())
    count = 0
    before = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    now = [0 for i in range(15)]
    for y in range(k):
        for i in range(1, n+1):
            now[i] = now[i-1] + before[i]
        count = now[n]
        for j in range(1, n+1):
            before[j] = now[j]
    result.append(count)

for i in result:
    print(i)