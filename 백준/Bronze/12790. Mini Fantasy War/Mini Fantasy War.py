"""
Mini Fantasy War
"""

t = int(input())

for i in range(t):
    num = list(map(int, input().split()))

    for j in range(4):
        num[j] += num[j + 4]

    if num[0] < 1:
        num[0] = 1
    if num[1] < 1:
        num[1] = 1
    if num[2] < 0:
        num[2] = 0

    print(num[0] + 5 * num[1] + 2 * num[2] + 2 * num[3])