"""
할로윈의 사탕
"""

t = int(input())

for i in range(t):
    c, v = map(int, input().split())

    print(f"You get {c // v} piece(s) and your dad gets {c % v} piece(s).")