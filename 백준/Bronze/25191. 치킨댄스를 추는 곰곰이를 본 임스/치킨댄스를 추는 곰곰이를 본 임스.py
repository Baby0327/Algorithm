n = int(input())
a, b = map(int, input().split())

tmp = a//2 + b

if n > tmp:
    print(tmp)
else:
    print(n)