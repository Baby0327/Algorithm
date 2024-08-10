"""
삼각수의 합
"""

num = [0]
total = 1

for i in range(301):
    num.append(num[-1] + total)
    total += 1

t = int(input())

for i in range(t):
    n = int(input())
    result = 0

    for j in range(n+1):
        result += (j) * num[j+1]

    print(result)