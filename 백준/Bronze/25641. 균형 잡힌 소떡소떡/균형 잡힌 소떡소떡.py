n = int(input())
s = input()

for i in range(n):
    now = s[i:]
    if now.count("s") == now.count("t"):
        print(now)
        break