N = int(input())
info = []

for i in range(N):
    size = list(map(int, input().split()))
    info.append(size)

result = []
for i in range(N):
    count = 0
    for j in range(N):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            count += 1
    result.append(count+1)

for i in result:
    print(i, end=" ")