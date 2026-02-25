import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    n = int(input())
    r = 0

    for i in range(n):
        r += int(input())
        r %= n

    print("NO" if r else "YES")