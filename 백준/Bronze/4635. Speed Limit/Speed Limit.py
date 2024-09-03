"""
Speed Limit
"""

while True:
    n = int(input())

    if n == -1:
        break

    mile = [[0, 0]]
    result = 0

    for i in range(n):
        mile.append(list(map(int, input().split())))
        result += mile[-1][0] * (mile[-1][-1] - mile[-2][-1])

    print(result, "miles")