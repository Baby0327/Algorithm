n, a = map(int, input().split())
num = list(map(int, input().split()))
print(sum(i // a for i in num))