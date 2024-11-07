a, b = input().split()
b = int(b)
p = a.index(".")
l = (len(a) - p - 1) * b
a = int(a[:p] + a[p + 1:])
result = str(a ** b)

if len(result) > l:
    print(result[:-l] + "." + result[-l:])
else:
    print("0." + "0" * (l - len(result)) + result)