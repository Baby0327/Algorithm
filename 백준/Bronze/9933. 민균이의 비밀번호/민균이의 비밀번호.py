"""
민균이의 비밀번호
"""

n = int(input())
word = []

for i in range(n):
    word.append(input())

for i in word:
    if i[::-1] in word:
        print(len(i), i[len(i)//2])
        break