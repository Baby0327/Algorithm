import sys
input = sys.stdin.readline

for i in range(int(input())):
    v = int(input())
    s = [int(input()) for _ in range(v)]
    print(sorted(s, key=lambda x : (-s.count(x), x))[0])