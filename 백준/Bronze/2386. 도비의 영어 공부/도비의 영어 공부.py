"""
도비의 영어 공부
"""

while True:
    n = input()
    x = n[0]
    w = n[2:]

    if x == "#":
        break

    print(f"{x} {w.count(x) + w.count(chr(ord(x) - 32))}")