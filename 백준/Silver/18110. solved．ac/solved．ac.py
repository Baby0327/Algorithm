import sys

n = int(sys.stdin.readline())
delete = n*0.15
if int(delete*10)%10 == 5 and int(delete)%10%2 == 0:
    delete = round(delete) + 1
else:
    delete = round(delete)

opinion = []
for i in range(n):
    opinion.append(int(sys.stdin.readline()))

opinion.sort()

opinion = opinion[delete:len(opinion)-delete]

if n != 0:
    result = sum(opinion)/len(opinion)
    if int(result * 10) % 10 == 5 and int(result)%10%2 == 0:
        print(round(result)+1)
    else:
        print(round(result))
else:
    print(0)