N = int(input())
sg = list(map(int, input().split()))
M = int(input())
result = list(map(int, input().split()))

count = [0 for i in range(10000000*2+1)]

for i in sg:
    count[i] += 1

for i in result:
    print(count[i], end=" ")