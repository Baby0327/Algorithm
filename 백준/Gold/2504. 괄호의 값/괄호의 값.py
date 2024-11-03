import sys
input = sys.stdin.readline

def calc(start, num):
    index.pop()
    temp = 0
    while True:
        p = l.pop()
        if p == start:
            break
        if type(p) == str:
            return 1
        temp += (p)
    if not temp:
        l.append(num)
    else:
        l.append(num * temp)

s = input().rstrip()
l = []
index = []

for i in s:
    if i == "(" or i == "[" or i.isdigit():
        index.append(len(l))
        l.append(i)
    elif i == ")" and index and l[index[-1]] == "(":
        check = calc("(", 2)
        if check:
            break
    elif i == "]" and index and l[index[-1]] == "[":
        check = calc("[", 3)
        if check:
            break
    else:
        l.append(i)

print(sum(l) if len([i for i in l if type(i) == int]) == len(l) else 0)