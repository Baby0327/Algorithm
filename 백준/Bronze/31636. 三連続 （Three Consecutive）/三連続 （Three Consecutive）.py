n = int(input())
s = sorted(input().split("x"), key=lambda x : -len(x))
print("Yes" if len(s[0]) >= 3 else "No")