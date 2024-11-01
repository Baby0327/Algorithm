a = int(input())
b = int(input())
n = (a + b) % 12
print(12 if n == 0 else n)