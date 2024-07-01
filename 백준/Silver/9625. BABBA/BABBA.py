A = 1
B = 0

k = int(input())

for i in range(k):
    tmp = A
    A = B
    B = B + tmp

print(A, B)