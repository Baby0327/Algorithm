result = []

while True:
    n = int(input())
    tmp = []
    if n == -1:
        break
    for i in range(1,n+1):
        if n % i == 0:
            tmp.append(i)
    result.append(tmp)

for j in result:
    total = 0
    for k in range(len(j)-1):
        total += j[k]
    if total == j[len(j)-1]:
        print(j[len(j)-1],"= ", end="")
        for x in range(len(j)-2):
            print(str(j[x])+" + ", end="")
        print(j[len(j)-2])
    else:
        print(str(j[len(j)-1])+" is NOT perfect.")