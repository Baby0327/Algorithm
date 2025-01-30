n = int(input())
s = input()
print(n - max(s.count("N"), s.count("S"), s.count("E"), s.count("W")))