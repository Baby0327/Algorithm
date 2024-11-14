import sys
input = sys.stdin.readline

n = int(input())
a = sorted([[int(input()), i] for i in range(n)])
print(max(a[i][1] - i for i in range(n)) + 1)