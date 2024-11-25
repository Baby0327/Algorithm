s = input()
result = 1

for i in range(len(s) - 1):
    if (s[i] in "aeiou" and s[i + 1] in "aeiou") or (s[i] not in "aeiou" and s[i + 1] not in "aeiou"):
        result = 0
        break

print(result)