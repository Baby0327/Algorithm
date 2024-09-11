"""
사분면
"""

n = int(input())
count = [0] * 5

for i in range(n):
    x, y = map(int, input().split())

    if not x or not y:
        count[0] += 1
    else:
        if x > 0 and y > 0:
            count[1] += 1
        elif x < 0 and y > 0:
            count[2] += 1
        elif x < 0 and y < 0:
            count[3] += 1
        else:
            count[4] += 1

for i in range(5):
    if i != 4:
        print(f"Q{i + 1}: {count[i + 1]}")
    else:
        print(f"AXIS: {count[0]}")