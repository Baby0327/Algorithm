from collections import deque

N = int(input())
line = list(map(int, input().split()))

result = []
number = deque([i for i in range(1, N+1)])

while len(number) != 0:
    tmp = number.popleft()
    result.append(tmp)
    if line[tmp-1] < 0:
        number.rotate(-line[tmp-1])
    else:
        number.rotate(-line[tmp - 1]+1)

for i in result:
    print(i, end=" ")