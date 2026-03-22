import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = int(input())
    print(1 if (a & (-a)) == a else 0)