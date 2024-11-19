check = 1

for i in input():
    if i not in "IOSHZXN":
        check = 0
        print("NO")
        break

if check:
    print("YES")