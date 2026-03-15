a = input()
b = input()
n = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
num = [n[ord(b[i // 2]) - 65] if i % 2 else n[ord(a[i // 2]) - 65] for i in range(len(a) * 2)]

while len(num) > 2:
    temp = []
    for i in range(len(num) - 1):
        temp.append(int(str(num[i] + num[i + 1])[-1]))
    num = temp

print("".join(map(str, num)))