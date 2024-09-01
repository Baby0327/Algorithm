"""
주사위 게임
"""

n = int(input())
player1, player2 = 100, 100

for i in range(n):
    dice1, dice2 = map(int, input().split())

    if dice1 > dice2:
        player2 -= dice1
    elif dice1 < dice2:
        player1 -= dice2

print(player1)
print(player2)