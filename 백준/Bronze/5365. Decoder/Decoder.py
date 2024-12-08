n = int(input())
s = input().split()
result = ""
temp = 0

for i in range(n):
    if len(s[i]) > temp:
        result += s[i][temp]
    else:
        result += " "
    temp = len(s[i]) - 1

print(result)