from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    stop = 1
    p = list(input().rstrip())
    n = int(input())
    num = input().rstrip()
    num = deque(num[1:-1].split(','))
    if n == 0:
        num = deque()
    test = True
    for j in p:
        if j == 'R':
            test = not test
        elif j == 'D':
            if len(num) == 0:
                print("error")
                stop = 0
                break
            else:
                if test:
                    num.popleft()
                else:
                    num.pop()
    if stop:
        if test:
            print('['+",".join(num)+']')
        else:
            num.reverse()
            print('['+",".join(num)+']')
    else:
        continue