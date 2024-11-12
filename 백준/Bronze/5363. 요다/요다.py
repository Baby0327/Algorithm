import sys
input = lambda : sys.stdin.readline().rstrip()

for i in range(int(input())):
    s = input().split()
    print(*(s[2:] + s[:2]))