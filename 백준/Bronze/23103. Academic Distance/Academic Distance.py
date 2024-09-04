"""
Academic Distance
"""

n = int(input())
location = [list(map(int, input().split()))]
result = 0

for i in range(n-1):
    point = list(map(int, input().split()))
    location.append(point)
    result += abs(location[-1][0] - location[-2][0]) + abs(location[-1][1] - location[-2][1])

print(result)