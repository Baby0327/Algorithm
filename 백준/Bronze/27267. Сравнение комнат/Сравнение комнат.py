a, b, c, d = map(int, input().split())
result1 = a * b
result2 = c * d

if result1 == result2:
    print("E")
elif result1 > result2:
    print("M")
else:
    print("P")