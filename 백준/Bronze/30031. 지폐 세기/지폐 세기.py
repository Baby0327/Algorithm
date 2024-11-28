import sys
input = sys.stdin.readline

money = {136 : 1000, 142 : 5000, 148 : 10000, 154 : 50000}
total = 0

for i in range(int(input())):
    w, h = map(int, input().split())
    total += money[w]

print(total)