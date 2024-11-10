import sys
input = lambda : sys.stdin.readline().rstrip()

s = list(input())

for i in range(int(input())):
    i1, i2 = map(int, input().split())
    c1 = s[i1]
    c2 = s[i2]
    s[i1] = c2
    s[i2] = c1

print("".join(s))