n = int(input())
s = input()
result = sorted([[i, s.count(i)] for i in s], key=lambda x : -x[1])
print(*result[0])