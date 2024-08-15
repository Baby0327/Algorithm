"""
좋은 자동차 번호판
"""

n = int(input())

for i in range(n):
    num1, num2 = input().split("-")
    total = 0
    for j in range(len(num1)):
        total += 26**(len(num1) - j - 1) * (ord(num1[j]) - 65)

    print("nice" if abs(total - int(num2)) <= 100 else "not nice")