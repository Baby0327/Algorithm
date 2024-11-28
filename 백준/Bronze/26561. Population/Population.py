import sys
input = sys.stdin.readline

for i in range(int(input())):
    p, t = map(int, input().split())
    print(p + t//4 - t//7)