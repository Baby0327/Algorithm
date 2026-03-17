s = [list(input().split()) for _ in range(int(input()))]
s.sort(key=lambda x : int(x[1]))
result = ""

for i in range(len(s)):
    c = s[i][0][int(s[i][2]) - 1]
    result += c.upper() if c.islower() else c

print(result)