import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
num = set(x)
maxi = max(num)
score = [0] * (maxi + 1)

for i in x:
    if i < maxi:
        for j in range(2 * i, maxi + 1, i):
            if j in num:
                score[i] += 1
                score[j] -= 1

for i in x:
    print(score[i], end=" ")