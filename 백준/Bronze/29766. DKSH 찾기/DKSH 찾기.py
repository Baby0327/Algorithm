s = input()
print(sum(1 for i in range(len(s) - 3) if s[i : i + 4] == "DKSH"))