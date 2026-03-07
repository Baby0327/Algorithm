n = [input() for _ in range(int(input()))]
s = sorted(n)

if n == s:
    print("INCREASING")
elif n == s[::-1]:
    print("DECREASING")
else:
    print("NEITHER")