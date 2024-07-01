T = int(input())

result = []
for i in range(T):
    Word = list(input())
    start = Word[0]
    end = Word[len(Word)-1]
    tmp = start+end
    result.append(tmp)

for i in result:
    print(i)