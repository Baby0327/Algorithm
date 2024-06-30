import sys

K, N = map(int, sys.stdin.readline().split())

LAN = []
for i in range(K):
    LAN.append(int(sys.stdin.readline().rstrip()))

LAN.sort()

left = 1
right = LAN[-1]

while left <= right:
    middle = (left + right) // 2
    count = 0
    for i in range(K):
        count += LAN[i]//middle

    if count < N:
        right = middle - 1
    else:
        left = middle + 1

print(right)