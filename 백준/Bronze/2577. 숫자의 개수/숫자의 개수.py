A = int(input())
B = int(input())
C = int(input())

num = list(str(A*B*C))

print(num.count("0"))

x = 1
for i in range(9):
    print(num.count(str(x)))
    x += 1