import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
n = int(input())
score = [0] * n

for i in range(n):
    for j in range(3):
        aa, bb, cc = map(int, input().split())
        score[i] += aa * a + bb * b + cc * c

print(max(score))