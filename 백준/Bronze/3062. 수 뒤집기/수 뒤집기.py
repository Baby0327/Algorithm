"""
수 뒤집기
"""

t = int(input())

for i in range(t):
    n = input()
    total = int(n) + int(n[::-1])

    print("YES" if total == int(str(total)[::-1]) else "NO")