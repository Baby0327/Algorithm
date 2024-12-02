n = int(input())
s = input()
t = input()
print(sum(1 for i in range(n) if s[i] != t[i]))