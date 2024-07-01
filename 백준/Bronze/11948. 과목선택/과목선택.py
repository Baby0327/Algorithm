score = []
for i in range(4):
    score.append(int(input()))

result = sum(score) - min(score)

score = 0
for i in range(2):
    tmp = int(input())
    if tmp > score:
        score = tmp

print(result + score)