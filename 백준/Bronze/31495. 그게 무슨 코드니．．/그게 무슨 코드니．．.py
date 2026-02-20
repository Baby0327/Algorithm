s = input()
print(s[1:-1] if len(s) > 2 and s[0] == s[-1] == "\"" else "CE")