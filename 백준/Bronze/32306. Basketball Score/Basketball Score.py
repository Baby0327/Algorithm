"""
Basketball Score
"""

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
team1 = num1[0] + num1[1] * 2 + num1[2] * 3
team2 = num2[0] + num2[1] * 2 + num2[2] * 3

if team1 > team2:
    print(1)
elif team1 < team2:
    print(2)
else:
    print(0)