import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [input().rstrip() for _ in range(n)]
b = [input().rstrip() for _ in range(m)]

for i in a:
    for j in b:
        print(f"{i} as {j}")