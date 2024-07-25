"""
Dedupe
"""

n = int(input())

for i in range(n):
    ab = input()
    result = ab[0]

    for j in ab:
        if result[-1] != j:
            result += j

    print(result)