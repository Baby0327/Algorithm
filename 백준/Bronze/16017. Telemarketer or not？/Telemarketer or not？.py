num = []
for i in range(4):
    num.append(int(input()))

if (num[0] in [8, 9]) and (num[1] == num[2]) and (num[3] in [8, 9]):
    print("ignore")
else:
    print("answer")