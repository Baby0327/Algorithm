"""
옥상 정원 꾸미기
"""

import sys
input = sys.stdin.readline

building = []
count = 0

for i in range(int(input())):
    now = int(input())

    while building:
        if building[-1] <= now:
            building.pop()
        else:
            break

    count += len(building)
    building.append(now)

print(count)