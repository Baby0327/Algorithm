import sys
input = sys.stdin.readline

for _ in range(int(input())):
    i, n = map(int, input().split())
    print(i, n * (n + 1) // 2 + n)