"""
윷놀이
"""

for i in range(3):
    case = list(map(int, input().split()))
    count = case.count(0)

    if count:
        print(chr(count + 64))
    else:
        print("E")