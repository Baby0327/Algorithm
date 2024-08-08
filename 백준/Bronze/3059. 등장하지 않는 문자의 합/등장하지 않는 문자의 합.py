"""
등장하지 않은 문자의 합
"""

t = int(input())
total = 26 * (65 + 90) // 2

for i in range(t):
    s = set(list(input()))
    result = total

    for j in s:
        result -= ord(j)

    print(result)