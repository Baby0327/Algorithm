"""
Cow Cotillion
"""

n = int(input())

for i in range(n):
    num, animal = input().split()

    temp = [animal[0]]

    for j in range(1, int(num)):
        if temp and temp[-1] == ">" and animal[j] == "<":
            temp.pop()
        else:
            temp.append(animal[j])

    print("illegal" if temp else "legal")