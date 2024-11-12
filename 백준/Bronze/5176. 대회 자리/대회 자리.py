import sys
input = sys.stdin.readline

for i in range(int(input())):
    p, m = map(int, input().split())
    l = set()

    for j in range(p):
        l.add(int(input()))

    print(p - len(l))