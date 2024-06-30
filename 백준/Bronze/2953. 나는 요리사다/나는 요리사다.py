num = 0
score = 0
for i in range(5):
    tmp = list(map(int, input().split()))
    tmp = sum(tmp)
    if tmp > score:
        score = tmp
        num = i+1

print(num, score)