from collections import deque

N, M = map(int, input().split())
location = list(map(int, input().split()))
test = [0 for i in range(N)]

for i in range(M):
    test[location[i]-1] = i+1

test = deque(test)

i = 1
result = 0
while i <= M:
    tmp = test.index(i)
    if tmp <= len(test)//2:
        test.rotate(-tmp)
        result += tmp
    else:
        test.rotate(len(test)-tmp)
        result += len(test)-tmp
    test.popleft()
    i += 1

print(result)