"""
짝수를 찾아라
"""

t = int(input())

for i in range(t):
    num = list(map(int, input().split()))
    result = [i for i in num if i % 2 == 0]

    print(sum(result), min(result))