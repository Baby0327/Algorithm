"""
단어 뒤집기
"""

t = int(input())

for i in range(t):
    print(*[i[::-1] for i in input().split()])