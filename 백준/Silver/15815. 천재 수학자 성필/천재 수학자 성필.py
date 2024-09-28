"""
천재 수학자 성필
"""

from collections import deque

s = input()
process = deque()

for i in s:
    if i == "+":
        b = int(process.pop())
        a = int(process.pop())
        process.append(a + b)
    elif i == "-":
        b = int(process.pop())
        a = int(process.pop())
        process.append(a - b)
    elif i == "*":
        b = int(process.pop())
        a = int(process.pop())
        process.append(a * b)
    elif i == "/":
        b = int(process.pop())
        a = int(process.pop())
        process.append(a // b)
    else:
        process.append(i)

print(process[0])