import sys

N = int(sys.stdin.readline())

result = 0
for i in range(N):
    word = list(sys.stdin.readline().rstrip())
    stack = [0]
    for j in word:
        if j == stack[-1]:
            stack.pop()
        else:
            stack.append(j)
    if len(stack) == 1:
        result += 1

print(result)