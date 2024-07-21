"""
주사위 게임
"""

import sys

n = int(sys.stdin.readline())
maxi = 0

for i in range(n):
    dice = sorted(list(map(int, sys.stdin.readline().split())))

    if dice[0] == dice[1] == dice[2]:
        maxi = max(maxi, 10000 + dice[0] * 1000)
    elif dice[0] == dice[1]:
        maxi = max(maxi, 1000 + dice[0] * 100)
    elif dice[0] == dice[2]:
        maxi = max(maxi, 1000 + dice[0] * 100)
    elif dice[1] == dice[2]:
        maxi = max(maxi, 1000 + dice[1] * 100)
    else:
        maxi = max(maxi, dice[2] * 100)

sys.stdout.write(str(maxi))