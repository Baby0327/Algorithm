a, b = map(int, input().split())
c, d = map(int, input().split())
h = a + c
y = b + d

if h < y:
    result = "Hanyang Univ."
elif h > y:
    result = "Yongdap"
else:
    result = "Either"

print(result)