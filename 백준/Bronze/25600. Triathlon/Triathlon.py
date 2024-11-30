import sys
input = sys.stdin.readline

score = []

for i in range(int(input())):
    a, d, g = map(int, input().split())
    score.append(2 * a**2 if a == d + g else a * (d + g))

print(max(score))