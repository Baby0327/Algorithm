x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())

a = x1*y2+ y1*x2
b = x2*y2

if a > b:
    tmp1 = a
    tmp2 = b
else:
    tmp1 = b
    tmp2 = a

while tmp2 != 0:
    tmp = tmp1%tmp2
    tmp1 = tmp2
    tmp2 = tmp

print(a//tmp1, b//tmp1)