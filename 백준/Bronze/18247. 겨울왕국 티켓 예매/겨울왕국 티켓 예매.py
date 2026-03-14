import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    n, m = map(int, input().split())

    if n < 12 or m < 4:
        print("-1\n")
    else:
        print(str(m * 11 + 4) + "\n")