"""
전투 드로이드 가격
"""

price = [350.34, 230.90, 190.55, 125.30, 180.90]
t = int(input())

for i in range(t):
    count = list(map(int, input().split()))
    total = 0

    for j in range(5):
        total += price[j] * count[j]

    print(f"${round(total, 2):.2f}")