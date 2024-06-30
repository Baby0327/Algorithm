zero = [1, 0, 1]
one = [0, 1, 1]
for i in range(38):
    zero.append(zero[-1]+zero[-2])
    one.append(one[-1]+one[-2])

t = int(input())
for i in range(t):
    num = int(input())
    print(zero[num], one[num])