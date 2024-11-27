n = int(input())
s1 = input()
s2 = input()
print(sum(1 for i in range(n) if s1[i] != s2[i]))