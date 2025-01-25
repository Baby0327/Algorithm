n = int(input())
print(chr((n % 8 if n % 8 != 0 else 8) + 96) + str(n // 8 + int(n % 8 != 0)))