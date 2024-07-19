"""
학식 사주기
"""

n = int(input())
menu = []

for i in range(n):
    menu.append(int(input()))

m = int(input())
total = 0

for i in range(m):
    total += menu[int(input()) - 1]

print(total)