"""
후위 표기식2
"""

n = int(input())
postfix = input()
value = []
stack = []

for i in range(n):
    value.append(int(input()))

for i in postfix:
    if i.isalpha():
        stack.append(value[ord(i)-65])
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a / b)

print(f"{stack[0]:.2f}")