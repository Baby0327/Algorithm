"""
옥상 정원 꾸미기
"""

from collections import deque
import sys
input = sys.stdin.readline

building = deque()
count = 0

for i in range(int(input())):
    now = int(input())

    while building:
        if building[0] <= now:
            building.popleft()
        elif building[-1] <= now:
            building.pop()
        else:
            break

    count += len(building)
    building.append(now)

print(count)