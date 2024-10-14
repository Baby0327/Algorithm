"""
Last Factorial Digit
"""

t = int(input())

for i in range(t):
    n = int(input())
    result = 1

    for j in range(1, n + 1):
        result *= j

    print(result % 10)