import sys
input = sys.stdin.readline

maxi = 0

for i in range(int(input())):
    a, b = map(int, input().split())
    maxi = max(maxi, a * b)

print(maxi)