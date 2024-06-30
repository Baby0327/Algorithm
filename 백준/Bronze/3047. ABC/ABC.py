num = list(map(int, input().split()))
word = input()

a = 0
b = 0
c = 0
for i in num:
    if i == min(num):
        a = i
    elif i == max(num):
        c = i
    else:
        b = i

for i in word:
    if i == "A":
        print(a, end=" ")
    elif i == "B":
        print(b, end=" ")
    else:
        print(c, end=" ")