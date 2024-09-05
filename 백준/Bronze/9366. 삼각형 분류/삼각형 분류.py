"""
삼각형 분류
"""

t = int(input())

for i in range(t):
    l = sorted(list(map(int, input().split())))

    if l[0] + l[1] <= l[2]:
        print(f"Case #{i + 1}: invalid!")
    elif l[0] == l[2]:
        print(f"Case #{i + 1}: equilateral")
    elif l[1] in (l[0], l[2]):
        print(f"Case #{i + 1}: isosceles")
    else:
        print(f"Case #{i + 1}: scalene")