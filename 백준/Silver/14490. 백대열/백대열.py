def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)


n, m = map(int, input().split(':'))
result = GCD(n, m)
print(f"{n//result}:{m//result}")