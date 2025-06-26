a, b = map(int, input().split())
acre = a * b / 4840
print(int(acre // 5) + int(acre % 5 > 0))