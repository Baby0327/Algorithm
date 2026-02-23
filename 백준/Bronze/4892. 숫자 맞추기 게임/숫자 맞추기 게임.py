cnt = 0

while 1:
    n = int(input())

    if n == 0:
        break

    n1 = 3 * n
    flag = n1 % 2 == 0
    n2 = n1//2 if flag else (n1+1)//2
    n3 = 3 * n2
    n4 = n3 // 9
    cnt += 1
    print(f"{cnt}. {'even' if flag else 'odd'} {n4}")