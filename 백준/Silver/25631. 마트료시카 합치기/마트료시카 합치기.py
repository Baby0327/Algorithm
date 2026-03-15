n = int(input())
a = list(map(int, input().split()))
s = set(a)
print(max(a.count(i) for i in s))