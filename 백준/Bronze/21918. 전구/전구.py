"""
전구
"""

n, m = map(int, input().split())
light = list(map(int, input().split()))

for i in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        light[b-1] = c
    elif a == 2:
        for i in range(b, c+1):
            if light[i-1] == 0:
                light[i-1] = 1
            else:
                light[i-1] = 0
    elif a == 3:
        light = light[:b-1] + [0]*(c-b+1) + light[c:]
    elif a == 4:
        light = light[:b-1] + [1]*(c-b+1) + light[c:]

print(*light)