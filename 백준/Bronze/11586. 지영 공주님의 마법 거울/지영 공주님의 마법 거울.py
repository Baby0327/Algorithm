n = int(input())
s = [input() for _ in range(n)]
k = int(input())

if k == 1:
    for i in range(n):
        print(s[i])
elif k == 2:
    for i in range(n):
        print(s[i][::-1])
elif k == 3:
    for i in range(n):
        print(s[n - i - 1])