result = 0

for i in range(int(input())):
    s = input()
    result += int("01" in s or "OI" in s)

print(result)