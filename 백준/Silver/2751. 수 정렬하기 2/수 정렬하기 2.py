import sys

n = int(input())
num = list()

for i in range(n):
    num.append(int(sys.stdin.readline()))

num = sorted(num)
# num.sort()

for i in range(n):
    print(num[i])