import sys

input = sys.stdin.readline

n = int(input())

score = [0]
for i in range(n):
    score.append(int(input()))

result = [0]
if n <= 2:
    print(sum(score))
else:
    result.append(score[1])
    result.append(score[1]+score[2])
    for i in range(2, n):
        tmp = max(result[i-2] + score[i] + score[i+1], result[i-1] + score[i+1])
        result.append(tmp)
    print(result[n])