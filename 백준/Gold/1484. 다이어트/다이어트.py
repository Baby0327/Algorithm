import sys
input = sys.stdin.readline

g = int(input())
s = 1
e = 2
result = []

while s < e:
    now = e**2 - s**2
    if now > g:
        s += 1
    else:
        if now == g:
            result.append(e)
        e += 1

print("\n".join(map(str, result)) if result else -1)