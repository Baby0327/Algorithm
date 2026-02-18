flag = True

for _ in range(int(input())):
    if int(input()) < 48:
        flag = False

print(flag)