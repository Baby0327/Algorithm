import sys

input = sys.stdin.readline

n = int(input())

straw = []
for i in range(n):
    straw.append(int(input()))

straw.sort(reverse=True)

i = 0
tmp = sum(straw[:3])
while True:
    if straw[i] < straw[i+1] + straw[i+2]:
        print(straw[i] + straw[i+1] + straw[i+2])
        break
    else:
        i += 1
        if i == n-2:
            print(-1)
            break