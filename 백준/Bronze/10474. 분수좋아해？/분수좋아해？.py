"""
분수좋아해?
"""

while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    print(f"{a // b} {a % b} / {b}")