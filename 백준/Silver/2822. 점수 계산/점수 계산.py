score = []

for i in range(8):
    n = int(input())
    score.append([n, i+1])

score.sort(reverse=True)

total = []
num = []
for i in range(5):
        total.append(score[i][0])
        num.append(score[i][1])

num.sort()

print(sum(total))

for i in range(4):
    print(num[i], end=" ")
print(num[4])