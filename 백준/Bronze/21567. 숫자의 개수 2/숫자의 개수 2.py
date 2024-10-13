"""
숫자의 개수 2
"""

a = int(input())
b = int(input())
c = int(input())
result = [0] * 10

for i in str(a * b * c):
        result[int(i)] += 1

for i in result:
    print(i)