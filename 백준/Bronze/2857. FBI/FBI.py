result = 0

for i in range(1, 6):
    name = input()
    if "FBI" in name:
        print(i, end=" ")
        result += 1

if result == 0:
    print("HE GOT AWAY!")