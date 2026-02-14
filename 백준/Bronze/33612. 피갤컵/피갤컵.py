n = int(input()) - 1
temp = 8 + n * 7
print(2024 + temp // 12 - int(temp % 12 == 0), temp % 12 + (12 if temp % 12 == 0 else 0))