import sys
input = sys.stdin.readline
print = sys.stdout.write

while 1:
    n = int(input())

    if n == 0:
        break

    a = (n // 10000) * 120
    b = (n // 1000 % 10) * 24
    c = (n // 100 % 10) * 6
    d = (n // 10 % 10) * 2
    e = n % 10

    print(str(a + b + c + d + e) + "\n")