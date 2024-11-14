import sys
input = sys.stdin.readline

def calc(list):
    total = 0

    for i in range(1, len(list), 2):
        total += max(list[i - 1] * list[i], list[i - 1] + list[i])

    if len(list) % 2:
        total += list[-1]

    return total

positive = []
negative = []

for i in range(int(input())):
    n = int(input())

    if n > 0:
        positive.append(n)
    else:
        negative.append(n)

positive.sort(reverse=True)
negative.sort()

print(calc(positive) + calc(negative))