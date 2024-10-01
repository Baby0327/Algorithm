"""
키로거
"""

from collections import deque
import sys
input = sys.stdin.readline

def func(l):
    result = deque()
    temp = deque()

    for j in l:
        if j == "<":
            if result:
                temp.appendleft(result.pop())
        elif j == ">":
            if temp:
                result.append(temp.popleft())
        elif j == "-":
            if result:
                result.pop()
        else:
            result.append(j)

    print("".join(result + temp))


for i in range(int(input())):
    func(input().rstrip())