"""
Left Beehind
"""

while True:
    a, b = map(int, input().split())

    if not a and not b:
        break

    if a + b == 13:
        print("Never speak again.")
    elif a > b:
        print("To the convention.")
    elif a == b:
        print("Undecided.")
    elif a < b:
        print("Left beehind.")