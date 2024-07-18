"""
괄호 끼워넣기
"""

s = input()
stack = []

for i in range(len(s)):
    if len(stack) and stack[-1] == "(" and s[i] == ")":
        stack.pop()
    else:
        stack.append(s[i])

print(len(stack))