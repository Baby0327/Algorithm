import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(str(sum(2 * i + 1 for i in range(a // b))) + "\n")