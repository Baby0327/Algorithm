"""
키로거
"""

from collections import deque

t = int(input())

for i in range(t):
    result = deque()
    temp = deque()
    l = input()

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

    print("".join(result) + "".join(temp))