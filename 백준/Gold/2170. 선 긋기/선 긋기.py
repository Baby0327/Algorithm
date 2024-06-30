import sys

N = int(sys.stdin.readline())
line = []
for i in range(N):
    line.append(list(map(int, sys.stdin.readline().rstrip().split())))

line.sort(key=lambda x: (x[0], x[1]))

i = 1
start = line[0][0]
end = line[0][1]
result = 0
while i < N:
    if start <= line[i][0] <= end:
        end = max(end, line[i][1])
    else:
        result += (end-start)
        start = line[i][0]
        end = line[i][1]
    i += 1

result += (end-start)
print(result)