s = input().split()
flag = 0

if s.count(s[0]) == 10:
    flag = 1
else:
    for i in range(9):
        temp = input().split()

        if temp.count(temp[0]) == 10:
            flag = 1
            break
        else:
            for j in range(10):
                if s[j] != " " and s[j] != temp[j]:
                    s[j] = " "
    if s.count(" ") != 10:
        flag = 1

print(flag)