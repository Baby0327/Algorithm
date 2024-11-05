s = input()
i = 0
result = ""

while i < len(s):
    result += s[i]
    if result[-1] in ("a", "e", "i", "o", "u"):
        i += 2
    i += 1

print(result)