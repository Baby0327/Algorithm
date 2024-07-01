from collections import deque

N, K = map(int, input().split())

list = deque([i+1 for i in range(N)])

result = []
while True:
    if len(list) != 0:
        list.rotate(-K+1)
        tmp = list.popleft()
        result.append(tmp)
    else:
        break

print("<", end="")
for i in range(len(result)-1):
    print(result[i], end=", ")
print(result[-1], end=">")