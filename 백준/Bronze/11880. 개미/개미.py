import sys
input = sys.stdin.readline

for i in range(int(input())):
    l = sorted(list(map(int, input().split())))
    print((l[0] + l[1])**2 + l[2]**2)