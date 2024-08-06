"""
홀짝홀짝
"""

n = int(input())
k = input()
count = [0, 0]

for i in k:
    if int(i) % 2 == 0:
        count[0] += 1
    else:
        count[1] += 1

if count[0] > count[1]:
    print(0)
elif count[0] < count[1]:
    print(1)
else:
    print(-1)