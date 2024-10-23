s = input()
print(10 + sum(5 if s[i-1] == s[i] else 10 for i in range(1, len(s))))