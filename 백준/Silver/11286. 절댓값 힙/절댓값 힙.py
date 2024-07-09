"""
절댓값 힙
"""

import sys
import heapq

n = int(sys.stdin.readline())
num = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        # [절댓값, 부호] 형태의 값을 함께 heap에 push
        sign = 1
        if x < 0:
            sign = -1
        heapq.heappush(num, [abs(x), sign])
    else:
        if num:
            temp = heapq.heappop(num)
            if temp[1] == -1:
                sys.stdout.write(str(-temp[0])+ "\n")
            else:
                sys.stdout.write(str(temp[0]) + "\n")
        else:
            sys.stdout.write("0\n")