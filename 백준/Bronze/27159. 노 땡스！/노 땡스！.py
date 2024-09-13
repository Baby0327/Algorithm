"""
노 땡스!
"""

n = int(input())
x = list(map(int, input().split()))
temp = [x[0]]
score = 0

for i in range(1, n):
    if x[i] - temp[-1] == 1:
        temp.append(x[i])
    else:
        score += temp[0]
        temp = [x[i]]

score += temp[0]

print(score)