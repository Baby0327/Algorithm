"""
꼬리를 무는 숫자 나열
"""

num1, num2 = map(int, input().split())
x1y1 = [(num1 - 1) // 4, (num1 - 1) % 4]
x2y2 = [(num2 - 1) // 4, (num2 - 1) % 4]
distance = abs(x1y1[0] - x2y2[0]) + abs(x1y1[1] - x2y2[1])

print(distance)