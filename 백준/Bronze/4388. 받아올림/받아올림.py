"""
받아올림
"""

while True:
    num1, num2 = input().split()

    if num1 == num2 == "0":
        break

    num1 = "0" * (10 - len(num1)) + num1
    num2 = "0" * (10 - len(num2)) + num2
    count, carry = 0, 0

    for a, b in zip(num1[::-1], num2[::-1]):
        if int(a) + int(b) + carry >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

    print(count)