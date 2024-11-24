import sys
input = sys.stdin.readline

total = 0

for i in range(int(input())):
    h, b, k = map(int, input().split())

    if b > h:
        total += (b - h) * k

print(total)